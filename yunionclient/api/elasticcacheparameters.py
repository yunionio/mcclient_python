from yunionclient.common import base

class Elasticcacheparameter(base.ResourceBase):
    pass


class ElasticcacheparameterManager(base.StandaloneManager):
    resource_class = Elasticcacheparameter
    keyword = 'elasticcacheparameter'
    keyword_plural = 'elasticcacheparameters'
    _columns = ["Id", "Name", "Description"]

