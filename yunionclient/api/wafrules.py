from yunionclient.common import base

class WafRule(base.ResourceBase):
    pass


class WafRuleManager(base.StandaloneManager):
    resource_class = WafRule
    keyword = 'waf_rule'
    keyword_plural = 'waf_rules'
    _columns = ["Id", "Name", "Status", "Priority", "Action", "Statement_Condition", "Statements"]

