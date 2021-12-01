from yunionclient.common import base

class AlertNotification(base.ResourceBase):
    pass


class AlertNotificationManager(base.StandaloneManager):
    resource_class = AlertNotification
    keyword = 'alert_notification'
    keyword_plural = 'alert_notifications'
    _columns = ["Id", "Name", "Type", "Is_Default", "Disable_Resolve_Message", "Send_Reminder", "Settings"]

