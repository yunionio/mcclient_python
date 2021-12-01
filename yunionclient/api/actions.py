
from yunionclient.common import base

class Action(base.ResourceBase):
    pass


class ActionManager(base.StandaloneManager):
    resource_class = Action
    keyword = 'action'
    keyword_plural = 'actions'
    _columns = []
    _admin_columns = []

