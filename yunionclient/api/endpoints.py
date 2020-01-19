from yunionclient.common import base
from yunionclient.common import exceptions


class Endpoint(base.ResourceBase):
    _region = None

    @property
    def region(self):
        pos = self._region.find('/')
        if pos == -1:
            return self._region
        return self._region[:pos]

    @region.setter
    def region(self, value):
        self._region = value

    @property
    def zone(self):
        pos = self._region.find('/')
        if pos == -1:
            return None
        return self._region[pos+1:]


class EndpointManager(base.IdentityManager):
    resource_class = Endpoint
    is_admin_api = True
    keyword = 'endpoint'
    keyword_plural = 'endpoints'
    _columns = ['ID', 'Region', 'Zone', 'Service_ID', 'Service_name',
                        'PublicURL', 'AdminURL', 'InternalURL']

    def get_service_endpoint_in_region(self, sid, region, zone=None):
        endpoints = self.list()
        for e in endpoints[0]:
            if e['region'] == region and e['service_id'] == sid \
                    and e['zone'] == zone:
                return e
        raise exceptions.NotFound(404, details=('No endpoint for %s in %s/%s' %
                                            (sid, region, zone)))
