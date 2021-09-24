from yunionclient.common import base

class MetadataBaseManager(base.StandaloneManager):
    keyword = 'metadata'
    keyword_plural = 'metadatas'
    _columns = ['ID', 'Key', 'value']
    _admin_columns = []

    def __init__(self, api, service_type, _version):
        self.api = api
        self.service_type = service_type
        self._version = _version


class MetadataManager(base.StandaloneManager):
    keyword = 'metadata'
    keyword_plural = 'metadatas'
    _columns = ['ID', 'Key', 'value']
    _admin_columns = []

    def get_module(self, service):
        if service == 'compute':
            return MetadataBaseManager(self.api, 'compute_v2', '')
        elif service == 'image':
            return MetadataBaseManager(self.api, 'image', 'v1')
        elif service == 'identity':
            return MetadataBaseManager(self.api, 'identity', 'v3')
        else:
            raise Exception('Invalid service type')


    def list(self, **kwargs):
        if 'service' in kwargs:
            return self.get_module(kwargs['service']).list()
        raise Exception('No service specified')

    def get(self, idstr, **kwargs):
        if 'service' in kwargs:
            return self.get_module(kwargs['service']).get(idstr)
        raise Exception('No service specified')

