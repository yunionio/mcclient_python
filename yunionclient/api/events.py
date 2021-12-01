from yunionclient.common import base

class Event(base.ResourceBase):
    pass


class EventManager(base.StandaloneManager):
    resource_class = Event
    keyword = 'event'
    keyword_plural = 'events'
    _columns = ["Id", "Ops_Time", "Obj_Id", "Obj_Type", "Obj_Name", "User", "User_Id", "Tenant", "Tenant_Id", "Owner_Tenant_Id", "Action", "Notes"]

