from yunionclient.common import base

class Elasticcache(base.ResourceBase):
    pass


class ElasticcacheManager(base.StandaloneManager):
    resource_class = Elasticcache
    keyword = "elasticcache" 
    keyword_plural = "elasticcaches"
    _columns = ["ID", "Name", "Cloudregion_Id", "Status", "InstanceType", "CapacityMB", "Engine", "EngineVersion"]
    _admin_columns = []
