from yunionclient.common import base

class Dbinstanceparameter(base.ResourceBase):
    pass


class DbinstanceparameterManager(base.StandaloneManager):
    resource_class = Dbinstanceparameter
    keyword = 'dbinstanceparameter'
    keyword_plural = 'dbinstanceparameters'
    _columns = ["Id", "Name", "Key", "Value", "Description"]

