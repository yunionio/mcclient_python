
from yunionclient.common import base

class Receiver(base.ResourceBase):
    pass


class ReceiverManager(base.StandaloneManager):
    resource_class = Receiver
    keyword = 'receiver'
    keyword_plural = 'receivers'
    _columns = []
    _admin_columns = []

