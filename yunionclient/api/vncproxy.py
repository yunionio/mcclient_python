from yunionclient.common import base


class VNCProxyManager(base.Manager):
    service_type = 'vncproxy'

    def connect(self, idstr, obj=None):
        if obj is None:
            url = r'/vncproxy/%s' % idstr
        else:
            url = r'/vncproxy/%s/%s' % (obj, idstr)
        resp, body = self.json_request('POST', url)
        return body['vncproxy']
