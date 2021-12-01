from yunionclient.common import base

class Nodealert(base.ResourceBase):
    pass


class NodealertManager(base.StandaloneManager):
    resource_class = Nodealert
    keyword = 'nodealert'
    keyword_plural = 'nodealerts'
    _columns = ["Id", "Type", "Metric", "Node_Name", "Node_Id", "Period", "Window", "Comparator", "Threshold", "Recipients", "Level", "Channel", "State", "Project_Id"]

