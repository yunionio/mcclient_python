
from yunionclient.common import base

class Task(base.ResourceBase):
    pass


class TaskManager(base.StandaloneManager):
    resource_class = Task
    keyword = 'task'
    keyword_plural = 'tasks'
    _columns = []
    _admin_columns = []

