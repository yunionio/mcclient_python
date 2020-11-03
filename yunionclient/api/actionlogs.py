from yunionclient.common import base

class Action(base.ResourceBase):
    pass


class ActionManager(base.LoggerManager):
    resource_class = Action
    keyword = "action" 
    keyword_plural = "actions"
    _columns = ["id", "start_time", "service", "ops_time", "obj_id", "obj_type", "obj_name", "user", "user_id", "tenant", "tenant_id", "owner_tenant_id", "action", "success", "notes"]
    _admin_columns = []
