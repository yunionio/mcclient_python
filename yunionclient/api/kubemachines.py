
from yunionclient.common import base

class Kubemachine(base.ResourceBase):
    pass


class KubemachineManager(base.StandaloneManager):
    resource_class = Kubemachine
    keyword = 'kubemachine'
    keyword_plural = 'kubemachines'
    _columns = []
    _admin_columns = []

