import json
import os

from yunionclient.common import base
from yunionclient.common import exceptions
from yunionclient.common import utils
from yunionclient.common.utils import url_unquote, url_quote


class Image(base.ResourceBase):

    def _normalize_attribute_dict(self, attr_dict):
        props = attr_dict.get('properties', {})
        new_props = {}
        for k, v in props.items():
            while k.startswith('_') or k.startswith('-'):
                k = k[1:]
            k = k.replace('-', '_')
            new_props[k] = v
        attr_dict['properties'] = new_props
        attr_dict.pop('os_arch', None)
        return attr_dict

    def _get_owner(self):
        if getattr(self, '_owner', None) is None:
            if self._client_api.is_admin():
                self._owner = self._client_api.tenants.get(self.owner)
            else:
                self._owner = None
        return self._owner

    @property
    def owner_name(self):
        owner = self._get_owner()
        if owner is not None:
            return owner.name
        else:
            return '[unknown]'

    @property
    def os_distribution(self):
        return self.properties.get('os_distribution', None)

    @property
    def os_version(self):
        return self.properties.get('os_version', None)

    @property
    def os_codename(self):
        return self.properties.get('os_codename', None)

    @property
    def os_arch(self):
        return self.properties.get('os_arch', None)

    @property
    def os_type(self):
        return self.properties.get('os_type', None)

    @property
    def preference(self):
        return int(self.properties.get('preference', '0'))

    @property
    def notes(self):
        return self.properties.get('notes', None)


class ImageManager(base.ImageManager):
    resource_class = Image
    keyword = 'image'
    keyword_plural = 'images'
    _columns = ['ID', 'Name', 'Tags', 'Disk_format', 'Size', 'Is_public',
                'OS_Type', 'OS_Distribution', 'OS_version',
                'Min_disk', 'Min_ram', 'Status',
                'Notes', 'OS_arch', 'Preference', 'OS_Codename',
                'Parent_id']
    _admin_columns = ['Owner', 'Owner_name']
    _meta_prefix = 'x-image-meta'
    _meta_property_prefix = 'x-image-meta-property'

    def get_meta(self, headers):
        meta = {}
        meta['properties'] = {}
        for (k, v) in headers.items():
            if k.startswith(self._meta_property_prefix):
                kn = k[len(self._meta_property_prefix) + 1:]
                meta['properties'][kn] = v
            elif k.startswith(self._meta_prefix):
                kn = k[len(self._meta_prefix) + 1:]
                meta[kn] = v
        return meta

    def set_meta(self, meta):
        headers = {}
        for (k, v) in meta.items():
            headers['%s-%s' % (self._meta_prefix, k)] = v
        return headers

    def set_property_meta(self, meta):
        headers = {}
        for (k, v) in meta.items():
            headers['%s-%s' % (self._meta_property_prefix, k)] = v
        return headers

    def list(self, **kwargs):
        url = r'/images'
        if len(kwargs) > 0:
            url += '?' + utils.urlencode(kwargs)
        return self._list(url, self.keyword_plural)

    def get_by_id(self, image_id):
        resp, body = self.json_request('HEAD', r'/images/%s' % image_id)
        for k, v in resp.items():
            resp[k] = url_unquote(v)
        return self._dict_to_object(self.get_meta(resp), None)

    def get_by_name(self, name):
        ret = None
        images = self.list({'name': name})
        for img in images[0]:
            if img.name == name:
                if ret is None:
                    ret = img
                else:
                    raise exceptions.Conflict(409,
                            details='More than one images named "%s"!' % name)
        if ret is not None:
            return ret
        raise exceptions.NotFound(404, details=('Image %s not found' % name))

    def get(self, image_id):
        try:
            return self.get_by_id(image_id)
        except exceptions.NotFound:
            return self.get_by_name(image_id)

    def get_image_history(self, idstr):
        url = r'/%s/%s/history' % (self.keyword_plural, idstr)
        resp, body = self.json_request('GET', url)
        response_key = 'image_history'
        data = body[response_key]
        return data

    def update(self, idstr, kwargs):
        if 'name' in kwargs:
            try:
                img = self.get_by_name(kwargs['name'])
                if img.id != idstr:
                    raise exceptions.Conflict(409,
                            details='Name "%s" duplicated!' % kwargs['name'])
            except exceptions.NotFound:
                pass
        img = self.get(idstr)
        headers = self.set_meta(kwargs)
        if img.properties is not None and len(img.properties) > 0:
            headers.update(self.set_property_meta(img.properties))
        for k, v in headers.items():
            headers[k] = url_quote(v)
        resp, body = self.json_request('PUT', r'/images/%s' % idstr,
                            headers=headers)
        for k, v in resp.items():
            resp[k] = url_unquote(v)
        return self._dict_to_object(body[self.keyword], None)

    def update_properties(self, idstr, **kwargs):
        headers = self.set_property_meta(kwargs)
        for k, v in headers.items():
            headers[k] = url_quote(v)
        resp, body = self.json_request('PUT', r'/images/%s' % idstr,
                            headers=headers)
        for k, v in resp.items():
            resp[k] = url_unquote(v)
        return self._dict_to_object(body[self.keyword], None)

    def download(self, idstr, fn):
        url = r'/images/%s' % idstr
        req = self.get_urllib2_raw_request(url)
        CHUNK = 16 * 1024
        import sys
        fp = sys.stdout
        if fn is not None and len(fn) > 0:
            try:
                fp = open(fn, 'wb')
            except:
                pass
        while True:
            chunk = req.read(CHUNK)
            if not chunk:
                break
            fp.write(chunk)
        fp.close()

    def upload(self, filename, name, fmt, public, kwargs=None):
        if not os.path.exists(filename):
            raise Exception('File %s not found')
        try:
            self.get_by_name(name)
            raise exceptions.Conflict(409,
                                details='Name "%s" exists!' % name)
        except exceptions.NotFound:
            pass
        headers = {}
        headers['x-image-meta-name'] = name
        headers['x-image-meta-disk-format'] = fmt
        headers['x-image-meta-size'] = '%d' % os.path.getsize(filename)
        headers['x-image-meta-container-format'] = 'bare'
        if public:
            headers['x-image-meta-is-public'] = 'true'
        else:
            headers['x-image-meta-is-public'] = 'false'
        if kwargs and (('docker_id' and 'docker_parent_id') in kwargs):
            headers['x-image-meta-docker-id'] = kwargs['docker_id']
            headers['x-image-meta-docker-parent-id'] = kwargs['docker_parent_id']
        if kwargs and 'tag' in kwargs:
            headers['x-image-meta-tag'] = kwargs['tag']
        import mmap
        with open(filename, 'rb') as f:
            body = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            resp, rbody = self.raw_request('POST', r'/images', headers=headers,
                                             body=body)
            body.close()
            body = json.loads(rbody)
            return self._dict_to_object(body[self.keyword], None)
        raise Exception('Unknown')

    def swap_location(self, id1, id2):
        url = r'/images/swap-location/%s' % id1
        headers = {}
        headers['x-image-meta-swap-image-id'] = id2
        self.raw_request('POST', url, headers=headers)

    def delete(self, idstr):
        resp, body = self.json_request('DELETE', r'/images/%s' % idstr)
        return body

    def add_tag(self, idstr, tag):
        url = r'/images/%s/tags/%s' % (idstr, tag)
        resp, body = self.json_request('POST', url)

    def delete_tag(self, idstr, tag):
        url = r'/images/%s/tags/%s' % (idstr, tag)
        resp, body = self.json_request('DELETE', url)

    def get_image_by_docker_id(self, idstr):
        url = r'/images/docker/%s' % idstr
        resp, body = self.json_request('GET', url)
        return body
