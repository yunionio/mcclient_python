from yunionclient.common import base

class Cloudpolicy(base.ResourceBase):
    pass


class CloudpolicyManager(base.CloudidManager):
    resource_class = Cloudpolicy
    keyword = 'cloudpolicy'
    keyword_plural = 'cloudpolicies'
    _columns = ["id","name","description","domain_id","domain","public_scope","policy_type","status","locked"]