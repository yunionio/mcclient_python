from yunionclient.common import base
from yunionclient.common import utils


class UsageManager(base.Manager):

    def get_guest_usage(self, idstr, typestr, **kwargs):
        url=r'/usages/%s' % (idstr, )
        if typestr is not None:
            query_str=utils.urlencode(kwargs)
            url += r'/%s?%s' % (typestr, query_str)
        resp, body = self.json_request('GET', url)
        return body

    def get_host_usage(self, idstr, typestr, **kwargs):
        url = r'/usages/hosts/%s' % (idstr, )
        if typestr is not None:
            query_str=utils.urlencode(kwargs)
            url += r'/%s?%s' % (typestr, query_str)
        resp, body = self.json_request('GET', url)
        return body

    def get_cluster_usage(self, idstr, typestr, **kwargs):
        url = r'/usages/clusters/%s/' % (idstr, )
        if typestr is not None:
            query_str=utils.urlencode(kwargs)
            url += r'/%s?%s' % (typestr, query_str)
        resp, body = self.json_request('GET', url)
        return body

    def get_zone_usage(self, idstr, typestr, **kwargs):
        url = r'/usages/zones/%s' % (idstr, )
        query_str = utils.urlencode(kwargs)
        if typestr is not None:
            url += r'/%s?%s' % (typestr, query_str)
        else:
            url += r'?%s' % query_str
        resp, body = self.json_request('GET', url)
        return body

    def get_usage_general(self):
        resp, body = self.json_request('GET', '/usages')
        return body
