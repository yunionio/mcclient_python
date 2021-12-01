from yunionclient.common import base

class Notification(base.ResourceBase):
    pass


class NotificationManager(base.StandaloneManager):
    resource_class = Notification
    keyword = 'notification'
    keyword_plural = 'notifications'
    _columns = ["Title", "Content", "Contacttype", "Priority", "Receiver_Details"]

