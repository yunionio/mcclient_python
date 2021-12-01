from yunionclient.common import base

class Meteralert(base.ResourceBase):
    pass


class MeteralertManager(base.StandaloneManager):
    resource_class = Meteralert
    keyword = 'meteralert'
    keyword_plural = 'meteralerts'
    _columns = ["Id", "Type", "Provider", "Account", "Account_Id", "Comparator", "Threshold", "Recipients", "Level", "Channel", "State", "Project_Id"]

