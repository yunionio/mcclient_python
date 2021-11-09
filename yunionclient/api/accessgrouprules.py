from yunionclient.common import base


class AccessGroupRuleManager(base.StandaloneManager):
    keyword = "access_group_rule" 
    keyword_plural = "access_group_rules"
    _columns = []
    _admin_columns = []
