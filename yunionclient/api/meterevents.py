from yunionclient.common import base

class MeterEvent(base.ResourceBase):
    pass


class MeterEventManager(base.MeterManager):
    resource_class = MeterEvent
    keyword = 'meter_event'
    keyword_plural = 'meter_events'
    _columns = ["id","ops_time","obj_id","obj_type","obj_name","user","user_id","tenant","tenant_id","owner_tenant_id","action","notes"]