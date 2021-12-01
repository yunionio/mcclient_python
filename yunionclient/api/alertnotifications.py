
from yunionclient.common import base

class AlertNotification(base.ResourceBase):
    pass


class AlertNotificationManager(base.StandaloneManager):
    resource_class = AlertNotification
    keyword = 'alert_notification'
    keyword_plural = 'alert_notifications'
    _columns = []
    _admin_columns = []

