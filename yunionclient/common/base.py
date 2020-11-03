# Copyright 2012 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Base utilities to build API operation managers and objects on top of.
"""

from yunionclient.common import utils


class Manager(object):
    """
    Managers interact with a particular type of API (servers, flavors, images,
    etc.) and provide CRUD operations for them.
    """
    resource_class = None
    service_type = 'compute_v2'
    is_admin_api = False
    _columns = None
    _admin_columns = None
    _version = ''

    def __init__(self, api):
        self.api = api

    @property
    def columns(self):
        cols = []
        cols.extend(self._columns)
        if self.api.is_system_admin() and self._admin_columns is not None:
            cols.extend(self._admin_columns)
        return cols

    def tenant_id(self):
        return self.api.get_default_tenant().get_id()

    def tenant_name(self):
        return self.api.get_default_tenant().get_name()

    def _get_versioned_url(self, url):
        if self._version is not None and len(self._version) > 0:
            while url.startswith('/'):
                url = url[1:]
            url = r'/%s/%s' % (self._version, url)
        return url

    def json_request(self, method, url, **kwargs):
        return self.api.json_request(self.service_type, self.is_admin_api,
                                method, self._get_versioned_url(url), **kwargs)

    def raw_request(self, method, url, **kwargs):
        return self.api.raw_request(self.service_type, self.is_admin_api,
                                method, self._get_versioned_url(url), **kwargs)

    def get_urllib2_raw_request(self, url, **kwargs):
        return self.api.get_urllib2_raw_request(self.service_type,
                    self.is_admin_api, self._get_versioned_url(url), **kwargs)

    def _dict_to_object(self, dict_obj, obj_class):
        cls = obj_class
        if cls is None:
            cls = self.resource_class
        if cls is not None:
            if isinstance(dict_obj, dict):
                return cls(self.api, dict_obj)
            elif isinstance(dict_obj, list):
                rets = []
                for o in dict_obj:
                    rets.append(self._dict_to_object(o, obj_class))
                return rets
        else:
            return dict_obj

    def _get(self, url, response_key, obj_class=None):
        resp, body = self.json_request('GET', url)
        data = body[response_key]
        return self._dict_to_object(data, obj_class)

    def _list(self, url, response_key, obj_class=None):
        resp, body = self.json_request('GET', url)

        if 'total' in body:
            total = body['total']
            if 'limit' in body:
                limit = body['limit']
            else:
                limit = 0
            if 'offset' in body:
                offset = body['offset']
            else:
                offset = 0
        else:
            total = 0
            limit = 0
            offset = 0
        data = body[response_key]
        return (self._dict_to_object(data, obj_class), total, limit, offset)

    def _create(self, url, body, response_key, obj_class=None):
        resp, body = self.json_request('POST', url, body=body)
        return self._dict_to_object(body[response_key], obj_class)

    def _delete(self, url, response_key, obj_class=None):
        resp, body = self.json_request('DELETE', url)
        # DELETE requests may not return a body
        if body is not None and response_key in body:
            return self._dict_to_object(body[response_key], obj_class)
        else:
            return None

    def _update(self, url, body, response_key, obj_class=None):
        resp, body = self.json_request('PUT', url, body=body)
        # PUT requests may not return a body
        if body is not None and response_key in body:
            return self._dict_to_object(body[response_key], obj_class)
        else:
            return None


def clean_kwargs(kwargs):
    newkw = {}
    for k in list(kwargs.keys()):
        if kwargs[k] is not None:
            newkw[k] = kwargs[k]
    return newkw


class StandaloneManager(Manager):

    @classmethod
    def keyword_url(cls):
        return cls.keyword.replace(':', '/')

    @classmethod
    def keyword_plural_url(cls):
        return cls.keyword_plural.replace(':', '/')

    def get(self, idstr, **kwargs):
        url = r'/%s/%s' % (self.keyword_plural_url(), idstr)
        newkw = clean_kwargs(kwargs)
        if len(newkw) > 0:
            url += '?' + utils.urlencode(newkw)
        return self._get(url, self.keyword)

    def get_specific(self, idstr, spec, **kwargs):
        url = r'/%s/%s/%s' % (self.keyword_plural_url(), idstr, spec)
        newkw = clean_kwargs(kwargs)
        if len(newkw) > 0:
            url += '?' + utils.urlencode(newkw)
        return self._get(url, self.keyword)

    def get_metadata(self, idstr, **kwargs):
        return self.get_specific(idstr, 'metadata', **kwargs)

    def set_metadata(self, idstr, **kwargs):
        return self.perform_action(idstr, 'metadata', **kwargs)

    def set_user_metadata(self, idstr, **kwargs):
        return self.perform_action(idstr, 'user-metadata', **kwargs)

    def get_descendent(self, idstr, desc_cls, desc_idstr, **kwargs):
        if desc_idstr is None:
            desc_idstr = '_'
        url = r'/%s/%s/%s/%s' % (self.keyword_plural_url(), idstr,
                                    desc_cls.keyword_plural_url(),
                                    desc_idstr)
        kwargs = clean_kwargs(kwargs)
        if len(kwargs) > 0:
            url += '?' + utils.urlencode(kwargs)
        return self._get(url, desc_cls.keyword)

    def get_descendent_specific(self, idstr, desc_cls, desc_idstr,
                                                        spec, **kwargs):
        if desc_idstr is None:
            desc_idstr = '_'
        url = r'/%s/%s/%s/%s/%s' % (self.keyword_plural_url(), idstr,
                                    desc_cls.keyword_plural_url(),
                                    desc_idstr, spec)
        kwargs = clean_kwargs(kwargs)
        if len(kwargs) > 0:
            url += '?' + utils.urlencode(kwargs)
        return self._get(url, desc_cls.keyword)

    def list(self, **kwargs):
        url = r'/%s' % (self.keyword_plural_url())
        kwargs = clean_kwargs(kwargs)
        if len(kwargs) > 0:
            url += '?' + utils.urlencode(kwargs)
        return self._list(url, self.keyword_plural)

    def list_descendent(self, idstr, *args, **kwargs):
        url = r'/%s/%s' % (self.keyword_plural_url(), idstr)
        if len(args) > 1:
            for i in range(0, len(args)-1, 2):
                url += r'/%s/%s' % (args[i].keyword_plural_url(), args[i+1])
        desc_cls = args[-1]
        url += '/' + desc_cls.keyword_plural_url()
        kwargs = clean_kwargs(kwargs)
        if len(kwargs) > 0:
            url += '?' + utils.urlencode(kwargs)
        return self._list(url, desc_cls.keyword_plural)

    def delete(self, idstr, **kwargs):
        url = r'/%s/%s' % (self.keyword_plural_url(), idstr)
        kwargs = clean_kwargs(kwargs)
        if len(kwargs) > 0:
            url += '?' + utils.urlencode(kwargs)
        return self._delete(url, self.keyword)

    def delete_descendent(self, idstr, desc_cls, desc_idstr, *args, **kwargs):
        if desc_idstr is None:
            desc_idstr = '_'
        url = r'/%s/%s/%s/%s' % (self.keyword_plural_url(), idstr,
                                    desc_cls.keyword_plural_url(),
                                    desc_idstr)
        if len(args) > 0:
            for i in range(0, len(args), 2):
                url += r'/%s/%s' % (args[i].keyword_plural_url(), args[i+1])
        kwargs = clean_kwargs(kwargs)
        if len(kwargs) > 0:
            url += '?' + utils.urlencode(kwargs)
        return self._delete(url, desc_cls.keyword)

    def create(self, **kwargs):
        return self.batch_create(1, **kwargs)

    def batch_create(self, count_, **kwargs):
        resp_key = self.keyword
        body = {}
        body[self.keyword] = kwargs
        if count_ > 1:
            resp_key = self.keyword_plural
            body['count'] = count_
        url = r'/%s' % (self.keyword_plural_url())
        return self._create(url, body, resp_key)

    def create_descendent(self, idstr, desc_cls, **kwargs):
        return self.batch_create_descendent(idstr, desc_cls, 1, **kwargs)

    def batch_create_descendent(self, idstr, desc_cls, count_, **kwargs):
        resp_key = self.keyword
        body = {}
        if count_ > 1:
            resp_key = self.keyword_plural
            body['count'] = count_
        body[desc_cls.keyword] = kwargs
        url = r'/%s/%s/%s' % (self.keyword_plural_url(), idstr,
                                    desc_cls.keyword_plural_url())
        return self._create(url, body, resp_key)

    def update(self, idstr, **kwargs):
        body = {}
        body[self.keyword] = kwargs
        if idstr is None:
            url = r'/%s' % self.keyword_plural_url()
        else:
            url = r'/%s/%s' % (self.keyword_plural_url(), idstr)
        return self._update(url, body, self.keyword)

    def update_descendent(self, idstr, desc_cls, desc_idstr, *args, **kwargs):
        if desc_idstr is None:
            desc_idstr = '_'
        url = r'/%s/%s/%s/%s' % (self.keyword_plural_url(), idstr,
                                    desc_cls.keyword_plural_url(), desc_idstr)
        if len(args) > 0:
            for i in range(0, len(args), 2):
                url += r'/%s/%s' % (args[i].keyword_plural_url(), args[i+1])

        body = {}
        body[desc_cls.keyword] = kwargs
        return self._update(url, body, desc_cls.keyword)

    def perform_action(self, idstr, action, **kwargs):
        url = r'/%s/%s/%s' % (self.keyword_plural_url(), idstr, action)
        body = {}
        body[self.keyword] = kwargs
        resp, body = self.json_request('POST', url, body=body)
        return body[self.keyword]

    def perform_class_action(self, action, **kwargs):
        url = r'/%s/%s' % (self.keyword_plural_url(), action)
        body = {}
        body[self.keyword] = kwargs
        resp, body = self.json_request('POST', url, body=body)
        return body[self.keyword]

    def perform_action_descendent(self, idstr, desc_cls, desc_idstr,
                                                        action, **kwargs):
        if desc_idstr is None:
            desc_idstr = '_'
        url = r'/%s/%s/%s/%s/%s' % (self.keyword_plural_url(), idstr,
                                desc_cls.keyword_plural_url(),
                                desc_idstr, action)
        body = {}
        body[desc_cls.keyword] = kwargs
        resp, body = self.json_request('POST', url, body=body)
        return body[desc_cls.keyword]


class ImageManager(StandaloneManager):
    service_type = 'image'
    _version = 'v1'


class JointManager(Manager):
    def get(self, mid, sid):
        url = r'/%s/%s/%s/%s' % (self.master_class().keyword_plural_url(),
                            mid, self.slave_class().keyword_plural_url(), sid)
        return self._get(url, self.keyword)

    def list(self, **kwargs):
        url = r'/%s-%s' % (self.master_class().keyword_plural_url(),
                            self.slave_class().keyword_plural_url())
        kwargs = clean_kwargs(kwargs)
        if len(kwargs) > 0:
            url += '?%s' % utils.urlencode(kwargs)
        return self._list(url, self.keyword_plural)

    def list_descendent(self, mid, **kwargs):
        url = r'/%s/%s/%s' % (self.master_class().keyword_plural_url(),
                            mid, self.slave_class().keyword_plural_url())
        kwargs = clean_kwargs(kwargs)
        if len(kwargs) > 0:
            url += '?%s' % utils.urlencode(kwargs)
        return self._list(url, self.keyword_plural)

    def attach(self, mid, sid, **kwargs):
        body = {}
        body[self.keyword] = kwargs
        url = r'/%s/%s/%s/%s' % (self.master_class().keyword_plural_url(),
                            mid, self.slave_class().keyword_plural_url(), sid)
        return self._create(url, body, self.keyword)

    def detach(self, mid, sid):
        url = r'/%s/%s/%s/%s' % (self.master_class().keyword_plural_url(),
                            mid, self.slave_class().keyword_plural_url(), sid)
        return self._delete(url, self.keyword)

    def update(self, mid, sid, **kwargs):
        body = {}
        body[self.keyword] = kwargs
        url = r'/%s/%s/%s/%s' % (self.master_class().keyword_plural_url(),
                            mid, self.slave_class().keyword_plural_url(), sid)
        return self._update(url, body, self.keyword)


class IdentityManager(StandaloneManager):
    service_type = 'identity'
    _version = 'v3'


class IdentityJointManager(JointManager):
    service_type = 'identity'
    _version = 'v3'


class ResourceBase(object):

    def __init__(self, api, attr_dict):
        self._client_api = api
        attr_dict = self._normalize_attribute_dict(attr_dict)
        for (k, v) in attr_dict.items():
            attr_name = k.replace('-', '_')
            setattr(self, attr_name, v)

    def _normalize_attribute_dict(self, attr_dict):
        return attr_dict

    def __repr__(self):
        reprkeys = sorted(k for k in list(self.__dict__.keys()) if k[0] != '_')
        info = ", ".join("%s=%s" % (k, getattr(self, k)) for k in reprkeys)
        return "<%s %s>" % (self.__class__.__name__, info)

    def __getitem__(self, key):
        if len(key) > 0 and key[0] != '_':
            return getattr(self, key, None)
        return None

    def get(self, key):
        return self[key]

    def to_dict(self):
        d = {}
        for k in dir(self):
            if k[0] != '_':
                v = getattr(self, k, None)
                if v is not None:
                    if not callable(v):
                        d[k] = v
        return d


class MeterManager(StandaloneManager):
    service_type = 'meter'

class LoggerManager(StandaloneManager):
    service_type = 'log'
