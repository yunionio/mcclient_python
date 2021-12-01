
from yunionclient.common import base

class Event(base.ResourceBase):
    pass


class EventManager(base.StandaloneManager):
    resource_class = Event
    keyword = 'event'
    keyword_plural = 'events'
    _columns = []
    _admin_columns = []

