from yunionclient.common import base

class Dbinstanceaccount(base.ResourceBase):
    pass


class DbinstanceaccountManager(base.StandaloneManager):
    resource_class = Dbinstanceaccount
    keyword = 'dbinstanceaccount'
    keyword_plural = 'dbinstanceaccounts'
    _columns = ["Id", "Name", "Dbinstance_Id", "Status", "Dbinstanceprivileges"]

