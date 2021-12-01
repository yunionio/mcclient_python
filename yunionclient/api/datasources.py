from yunionclient.common import base

class Datasource(base.ResourceBase):
    pass


class DatasourceManager(base.StandaloneManager):
    resource_class = Datasource
    keyword = 'datasource'
    keyword_plural = 'datasources'
    _columns = ["Id", "Name", "Type", "Url"]

