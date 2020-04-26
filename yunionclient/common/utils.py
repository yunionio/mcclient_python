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

import os
import uuid
import time
import urllib.request, urllib.parse, urllib.error
import logging
import hashlib
import mmap

from yunionclient.common import exceptions
from yunionclient.openstack.common import importutils
from functools import reduce


# Decorator for cli-args
def arg(*args, **kwargs):
    def _decorator(func):
        # Because of the sematics of decorator composition if we just append
        # to the options list positional options will appear to be backwards.
        func.__dict__.setdefault('arguments', []).insert(0, (args, kwargs))
        return func
    return _decorator


def pretty_choice_list(l):
    return ', '.join("'%s'" % i for i in l)


def get_value_ignorecase(dictobj, key):
    for k in list(dictobj.keys()):
        if k.lower() == key.lower():
            return dictobj[k]
    return None

def get_attribute_ignorecase(obj, key):
    for a in obj.__dict__:
        if a.lower() == key().lower():
            return getattr(obj, a, None)
    return None

def print_list(data, fields=None, formatters={}):
    if isinstance(data, list):
        objs = data
        if len(objs) > 1:
            title = 'Total: %d' % len(objs)
        else:
            title = None
    else:
        (objs, total, limit, offset) = data
        if limit > 0:
            pages = int(total)/limit
            if pages*limit < total:
                pages += 1
            page = (offset/limit) + 1
            title = 'Total: %d Pages: %d Limit: %d Offset: %d Page: %d' % \
                    (int(total), pages, limit, offset, page)
        else:
            title = 'Total: %d' % len(objs)
    if fields is None or len(fields) == 0:
        fields = []
        for o in objs:
            for k in list(o.keys()):
                k = k.upper()
                if k not in fields:
                    fields.append(k)
    import prettytable
    pt = prettytable.PrettyTable(fields, caching=False)
    pt.align = 'l'
    from yunionclient.common.base import ResourceBase
    data_fields_tbl = {}
    for o in objs:
        row = []
        for field in fields:
            if field in formatters:
                row.append(formatters[field](o))
            else:
                field_name = field.lower().replace(' ', '_')
                if isinstance(o, ResourceBase):
                    o = o.to_dict()
                if isinstance(o, dict):
                    data = get_value_ignorecase(o, field_name)
                else:
                    data = get_attribute_ignorecase(o, field_name)
                if data is None:
                    data = ''
                elif field not in data_fields_tbl:
                    data_fields_tbl[field] = True
                row.append(data)
        pt.add_row(row)

    data_fields = [f for f in fields if f in data_fields_tbl]
    print(pt.get_string(fields=data_fields)) #sortby=fields[0])
    if title is not None:
        print('****', title, '****')


def pretty_value(val):
    ret = ''
    if isinstance(val, dict):
        for k, v in val.items():
            if len(ret) > 0:
                ret += ','
            ret += '%s:%s' % (k, pretty_value(v))
        ret = '{%s}' % ret
    elif isinstance(val, list):
        for k in val:
            if len(ret) > 0:
                ret += ','
            ret += '%s' % (pretty_value(k))
        ret = '[%s]' % ret
    else:
        ret = '%s' % val
    return ret


def truncate(val, vlen):
    if len(val) < vlen:
        return val
    else:
        return val[:vlen] + '...'


def print_dict(d):
    import prettytable
    pt = prettytable.PrettyTable(['Property', 'Value'], caching=False)
    pt.aligns = ['l', 'l']
    from yunionclient.common.base import ResourceBase
    if isinstance(d, ResourceBase):
        d = d.to_dict()
    elif not isinstance(d, dict):
        dd = {}
        for k in list(d.__dict__.keys()):
            if k[0] != '_':
                v = getattr(d, k)
                if not callable(v):
                    dd[k] = v
        d = dd
    for k, v in d.items():
        v = pretty_value(v)
        row = [k, v]
        pt.add_row(row)
    print(pt.get_string(sortby='Property'))


def find_resource(manager, name_or_id):
    """Helper for the _find_* methods."""
    # first try to get entity as integer id
    try:
        if isinstance(name_or_id, int) or name_or_id.isdigit():
            return manager.get(int(name_or_id))
    except exceptions.NotFound:
        pass

    # now try to get entity as uuid
    try:
        uuid.UUID(str(name_or_id))
        return manager.get(name_or_id)
    except (ValueError, exceptions.NotFound):
        pass

    # finally try to find entity by name
    try:
        return manager.find(name=name_or_id)
    except exceptions.NotFound:
        msg = "No %s with a name or ID of '%s' exists." % \
              (manager.resource_class.__name__.lower(), name_or_id)
        raise exceptions.CommandError(msg)


def skip_authentication(f):
    """Function decorator used to indicate a caller may be unauthenticated."""
    f.require_authentication = False
    return f


def is_authentication_required(f):
    """Checks to see if the function requires authentication.

    Use the skip_authentication decorator to indicate a caller may
    skip the authentication step.
    """
    return getattr(f, 'require_authentication', True)


def string_to_bool(arg):
    return arg.strip().lower() in ('t', 'true', 'yes', '1')


def env(*vars, **kwargs):
    """Search for the first defined of possibly many env vars

    Returns the first environment variable defined in vars, or
    returns the default defined in kwargs.
    """
    for v in vars:
        value = os.environ.get(v, None)
        if value:
            return value
    return kwargs.get('default', '')


def import_module(submodule=None):
    module = 'yunionclient'
    if submodule:
        module = '.'.join((module, submodule))
    return importutils.import_module(module)

def timestr_2_epoch(time_str, zone_index=8):
    return int(time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S')))+3600*zone_index

def confirm(prompt=""):
    try:
        c = input(prompt).strip()
        a = ['', 'Y', 'y']
        if c in a:
            return True
    except Exception as e:
        logging.error(e)

def urlencode(data):
    assert(isinstance(data, dict))
    kw_list = []
    for k in list(data.keys()):
        if data[k] is not None:
            if isinstance(data[k], list):
                for v in data[k]:
                    kw_list.append({k: v})
            else:
                kw_list.append({k: data[k]})
    kw_list = sorted(kw_list, key=lambda x: list(x.keys())[0])
    return '&'.join(map(urllib.parse.urlencode, kw_list))


def import_dsa_private_key(str):
    from Crypto.Util import asn1
    from Crypto.PublicKey import DSA
    seq2 = asn1.DerSequence()
    data = "\n".join(str.strip().split("\n")[1:-1]).decode("base64")
    seq2.decode(data)
    p, q, g, y, x = seq2[1:]
    key2 = DSA.construct((y, g, p, q, x))
    return key2

def export_dsa_public_key(key):
    import struct
    import binascii
    from Crypto.Util.number import long_to_bytes
    tup1 = [long_to_bytes(x) for x in (key.p, key.q, key.g, key.y)]

    def func(x):
        if (ord(x[0]) & 0x80):
            return chr(0) + x
        else:
            return x

    tup2 = list(map(func, tup1))
    keyparts = [str('ssh-dss')] + tup2
    keystring = str('').join(
                            [struct.pack(">I", len(kp)) + kp for kp in keyparts]
                            )
    return str('ssh-dss ') + binascii.b2a_base64(keystring)[:-1]

def decrypt_dsa(privkey, secret):
    key = import_dsa_private_key(privkey)
    assert(key.has_private())
    return decrypt_aes(export_dsa_public_key(key.publickey()), secret)

def decrypt_rsa(privkey, secret):
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    key = RSA.importKey(privkey)
    cipher = PKCS1_OAEP.new(key)
    message = cipher.decrypt(secret)
    return message

def decrypt(privkey, secret):
    try:
        return decrypt_rsa(privkey, secret)
    except:
        return decrypt_dsa(privkey, secret)

def decrypt_base64(privkey, secret):
    import base64
    return decrypt(privkey, base64.b64decode(secret))

def to_aes_key(key):
    while len(key) < 32:
        key += '$'
    if len(key) > 32:
        key = key[:32]
    return key

def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    return reduce(lambda x,y:x+y, lst)

def decrypt_aes(key, secret):
    from Crypto.Cipher import AES
    iv = secret[:AES.block_size]
    secret = secret[AES.block_size:]
    cipher = AES.new(to_aes_key(key), AES.MODE_CFB, iv)
    res = cipher.decrypt(secret)
    # print toHex(iv), toHex(secret), toHex(res), res
    return res

def decrypt_aes_base64(key, secret):
    import base64
    return decrypt_aes(key, base64.b64decode(secret))

def parse_isotime(expires):
    from datetime import datetime
    return datetime.strptime(expires+"UTC", '%Y-%m-%dT%H:%M:%S.%fZ%Z')

def get_paging_info(args):
    info = {}
    if args.limit:
        info['limit'] = int(args.limit)
    if args.offset:
        info['offset'] = int(args.offset)
    if args.order_by:
        info['order_by'] = args.order_by
        if args.order:
            info['order'] = args.order
    if args.details:
        info['details'] = True
    else:
        info['details'] = False
    if args.search:
        info['search'] = args.search
    if getattr(args, 'meta', False):
        info['with_meta'] = True
    if getattr(args, 'filter', None) and len(args.filter) > 0:
        idx = 0
        for f in args.filter:
            info['filter.%d' % idx] = f
            idx += 1
        if args.filter_any:
            info['filter_any'] = True
    if getattr(args, 'admin', False):
        info['admin'] = True
    if getattr(args, 'system', False):
        info['system'] = True
    tenant = getattr(args, 'tenant', None)
    if tenant is not None:
        info['admin'] = True
        info['tenant'] = tenant
    user = getattr(args, 'user', None)
    if user is not None:
        info['admin'] = True
        info['user'] = user
    if getattr(args, 'field', None) and len(args.field) > 0:
        idx = 0
        for f in args.field:
            info['field.%d' % idx] = f
            idx += 1
    return info

def md5sum(filename):
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(128*md5.block_size), b''):
            md5.update(chunk)
    return md5.hexdigest()

def md5sum_m(body):
    md5 = hashlib.md5()
    md5.update(body)
    return md5.hexdigest()


class mmap_open(object):
    def __init__(self, fd, length=0, **kwarg):
        self.fd = fd
        self.length = length
        # kwarg contains optionally offset argument for mmap
        self.kwarg = kwarg

    def __enter__(self):
        self.body = mmap.mmap(self.fd.fileno(), self.length,
                               access=mmap.ACCESS_READ, **self.kwarg)
        return self.body

    def __exit__(self, type, value, traceback):
        if self.body is not None:
            self.body.close()


def mkdir_p(path):
    offset = 1
    path = os.path.abspath(path)
    while offset < len(path):
        pos = path.find('/', offset)
        if pos < 0:
            pos = len(path)
        p_path = path[:pos]
        if os.path.exists(p_path):
            if not os.path.isdir(p_path):
                raise Exception('%s not a directory' % p_path)
        else:
            os.mkdir(p_path)
        offset = pos + 1


def string_to_boolean(string):
    if string.lower() in ['true', 'yes', 'enable']:
        return True
    else:
        return False


def random_password(num):
    import string
    import random
    chars = string.digits + string.letters
    npass = ''
    for i in range(num):
        npass += random.choice(chars)
    return npass

def td_total_seconds(td):
    return td.days*86400 + td.seconds

def ensure_unicode(s):
    if not isinstance(s, str):
        s = '%s' % s
    if isinstance(s, str):
        return s
    else:
        return s.decode('utf-8')

def ensure_ascii(s):
    if not isinstance(s, str):
        s = '%s' % s
    if isinstance(s, str):
        return s
    else:
        return s.encode('utf-8')

def ensure_bool(s):
    if isinstance(s, bool):
        return s
    elif isinstance(s, int) or isinstance(s, float):
        if s > 0:
            return True
        else:
            return False
    else:
        if not isinstance(s, str):
            s = '%s' % s
        if s.lower() in ['true', 'yes', '1']:
            return True
        else:
            return False

# https://tools.ietf.org/rfc/rfc3986.txt
# Uniform Resource Identifier (URI): Generic Syntax
# RFC 2396 is deprecated
def url_quote(s):
    if isinstance(s, str):
        s = s.encode('utf-8')
    return urllib.parse.quote(s)

def url_unquote(s):
    return urllib.parse.unquote(s)

def url_join(*args):
    args = list(map(ensure_ascii, args))
    args = list(map(urllib.parse.quote, args))
    return '/'.join(args)

def file_get_contents(fn):
    try:
        with open(fn, 'r') as f:
            return f.read()
    except Exception as e:
        logging.error("Error %s while reading %s" % (str(e), fn))
    return None
