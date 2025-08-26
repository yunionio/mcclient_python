from yunionclient.common import base

class Notifytemplate(base.ResourceBase):
    pass


class NotifytemplateManager(base.NotifyManager):
    resource_class = Notifytemplate
    keyword = 'notifytemplate'
    keyword_plural = 'notifytemplates'
    _columns = ["Id", "Name", "Contact_Type", "Topic", "Template_Type", "Content", "Example"]

