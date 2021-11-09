from yunionclient.common import base

class AccessGroupManager(base.StandaloneManager):
    keyword = "access_group" 
    keyword_plural = "access_groups"
    _columns = []
    _admin_columns = []
