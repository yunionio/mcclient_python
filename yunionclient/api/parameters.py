
from yunionclient.common import base

class Parameter(base.ResourceBase):
    pass


class ParameterManager(base.StandaloneManager):
    resource_class = Parameter
    keyword = 'parameter'
    keyword_plural = 'parameters'
    _columns = []
    _admin_columns = []

