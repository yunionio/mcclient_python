from yunionclient.common import base

class Elasticcacheaccount(base.ResourceBase):
    pass


class ElasticcacheaccountManager(base.StandaloneManager):
    resource_class = Elasticcacheaccount
    keyword = 'elasticcacheaccount'
    keyword_plural = 'elasticcacheaccounts'
    _columns = ["Id", "Name", "Description"]

