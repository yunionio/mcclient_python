
from yunionclient.common import base

class Serviceaccount(base.ResourceBase):
    pass


class ServiceaccountManager(base.StandaloneManager):
    resource_class = Serviceaccount
    keyword = 'serviceaccount'
    keyword_plural = 'serviceaccounts'
    _columns = []
    _admin_columns = []

