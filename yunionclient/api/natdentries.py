
from yunionclient.common import base

class Natdentry(base.ResourceBase):
    pass


class NatdentryManager(base.StandaloneManager):
    resource_class = Natdentry
    keyword = 'natdentry'
    keyword_plural = 'natdentries'
    _columns = []
    _admin_columns = []

