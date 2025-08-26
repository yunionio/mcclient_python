from yunionclient.common import base

class Subscriber(base.ResourceBase):
    pass


class SubscriberManager(base.NotifyManager):
    resource_class = Subscriber
    keyword = 'subscriber'
    keyword_plural = 'subscribers'
    _columns = ["Id", "Name", "Topic_Id", "Type", "Resource_Scope", "Role_Scope", "Receivers", "Role", "Robot"]

