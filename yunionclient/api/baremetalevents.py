from yunionclient.common import base

class Baremetalevent(base.ResourceBase):
    pass


class BaremetaleventManager(base.StandaloneManager):
    resource_class = Baremetalevent
    keyword = 'baremetalevent'
    keyword_plural = 'baremetalevents'
    _columns = ["Id", "Host_Id", "Host_Name", "Ipmi_Ip", "Created", "Event_Id", "Message", "Severity", "Type"]

