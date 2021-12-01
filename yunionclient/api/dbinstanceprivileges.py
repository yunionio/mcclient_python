
from yunionclient.common import base

class Dbinstanceprivilege(base.ResourceBase):
    pass


class DbinstanceprivilegeManager(base.StandaloneManager):
    resource_class = Dbinstanceprivilege
    keyword = 'dbinstanceprivilege'
    keyword_plural = 'dbinstanceprivileges'
    _columns = []
    _admin_columns = []

