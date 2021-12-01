from yunionclient.common import base

class Federatedrole(base.ResourceBase):
    pass


class FederatedroleManager(base.StandaloneManager):
    resource_class = Federatedrole
    keyword = 'federatedrole'
    keyword_plural = 'federatedroles'
    _columns = ["Federatednamespace_Id"]

