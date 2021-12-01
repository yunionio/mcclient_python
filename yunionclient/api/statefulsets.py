
from yunionclient.common import base

class Statefulset(base.ResourceBase):
    pass


class StatefulsetManager(base.StandaloneManager):
    resource_class = Statefulset
    keyword = 'statefulset'
    keyword_plural = 'statefulsets'
    _columns = []
    _admin_columns = []

