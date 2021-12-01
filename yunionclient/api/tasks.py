from yunionclient.common import base

class Task(base.ResourceBase):
    pass


class TaskManager(base.StandaloneManager):
    resource_class = Task
    keyword = 'task'
    keyword_plural = 'tasks'
    _columns = ["Id", "Obj_Name", "Obj_Id", "Task_Name", "Stage", "Created_At"]

