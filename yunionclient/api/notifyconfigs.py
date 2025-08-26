from yunionclient.common import base

class Notifyconfig(base.ResourceBase):
    pass


class NotifyconfigManager(base.NotifyManager):
    resource_class = Notifyconfig
    keyword = 'notifyconfig'
    keyword_plural = 'notifyconfigs'
    _columns = ["Name", "Type", "Content", "Attribution", "Project_Domain"]

