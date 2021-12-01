
from yunionclient.common import base

class Scopedpolicybinding(base.ResourceBase):
    pass


class ScopedpolicybindingManager(base.StandaloneManager):
    resource_class = Scopedpolicybinding
    keyword = 'scopedpolicybinding'
    keyword_plural = 'scopedpolicybindings'
    _columns = []
    _admin_columns = []

