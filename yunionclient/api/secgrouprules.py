
from yunionclient.common import base

class Secgrouprule(base.ResourceBase):
    pass


class SecgroupruleManager(base.StandaloneManager):
    resource_class = Secgrouprule
    keyword = 'secgrouprule'
    keyword_plural = 'secgrouprules'
    _columns = []
    _admin_columns = []

