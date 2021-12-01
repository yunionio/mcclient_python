
from yunionclient.common import base

class Subscriber(base.ResourceBase):
    pass


class SubscriberManager(base.StandaloneManager):
    resource_class = Subscriber
    keyword = 'subscriber'
    keyword_plural = 'subscribers'
    _columns = []
    _admin_columns = []

