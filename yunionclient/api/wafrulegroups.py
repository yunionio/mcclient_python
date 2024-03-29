from yunionclient.common import base

class WafRuleGroup(base.ResourceBase):
    pass


class WafRuleGroupManager(base.StandaloneManager):
    resource_class = WafRuleGroup
    keyword = 'waf_rule_group'
    keyword_plural = 'waf_rule_groups'
    _columns = ["Id", "Name", "Status", "Domain_Id", "Domain", "Is_System", "Rules"]

