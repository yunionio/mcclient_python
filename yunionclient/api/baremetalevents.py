
from yunionclient.common import base

class Baremetalevent(base.ResourceBase):
    pass


class BaremetaleventManager(base.StandaloneManager):
    resource_class = Baremetalevent
    keyword = 'baremetalevent'
    keyword_plural = 'baremetalevents'
    _columns = []
    _admin_columns = []

