
from yunionclient.common import base

class Natsentry(base.ResourceBase):
    pass


class NatsentryManager(base.StandaloneManager):
    resource_class = Natsentry
    keyword = 'natsentry'
    keyword_plural = 'natsentries'
    _columns = []
    _admin_columns = []

