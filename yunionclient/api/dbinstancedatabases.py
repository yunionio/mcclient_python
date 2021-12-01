from yunionclient.common import base

class Dbinstancedatabase(base.ResourceBase):
    pass


class DbinstancedatabaseManager(base.StandaloneManager):
    resource_class = Dbinstancedatabase
    keyword = 'dbinstancedatabase'
    keyword_plural = 'dbinstancedatabases'
    _columns = ["Id", "Name", "Character_Set", "Dbinstance_Id", "Dbinstance", "Status"]

