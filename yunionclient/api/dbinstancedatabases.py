
from yunionclient.common import base

class Dbinstancedatabase(base.ResourceBase):
    pass


class DbinstancedatabaseManager(base.StandaloneManager):
    resource_class = Dbinstancedatabase
    keyword = 'dbinstancedatabase'
    keyword_plural = 'dbinstancedatabases'
    _columns = []
    _admin_columns = []

