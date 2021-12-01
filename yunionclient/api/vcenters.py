
from yunionclient.common import base

class Vcenter(base.ResourceBase):
    pass


class VcenterManager(base.StandaloneManager):
    resource_class = Vcenter
    keyword = 'vcenter'
    keyword_plural = 'vcenters'
    _columns = []
    _admin_columns = []

