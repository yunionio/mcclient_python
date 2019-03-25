from yunionclient.common import base


class MetadataManager(base.StandaloneManager):
    keyword = 'metadata'
    keyword_plural = 'metadatas'
    _columns = ['ID', 'Key', 'value']
    _admin_columns = []
