
from yunionclient.common import base

class Cloudevent(base.ResourceBase):
    pass


class CloudeventManager(base.StandaloneManager):
    resource_class = Cloudevent
    keyword = 'cloudevent'
    keyword_plural = 'cloudevents'
    _columns = []
    _admin_columns = []

