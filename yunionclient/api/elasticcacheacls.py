from yunionclient.common import base

class Elasticcacheacl(base.ResourceBase):
    pass


class ElasticcacheaclManager(base.StandaloneManager):
    resource_class = Elasticcacheacl
    keyword = 'elasticcacheacl'
    keyword_plural = 'elasticcacheacls'
    _columns = ["Id", "Name", "Description"]

