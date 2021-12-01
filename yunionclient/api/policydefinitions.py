from yunionclient.common import base

class PolicyDefinition(base.ResourceBase):
    pass


class PolicyDefinitionManager(base.StandaloneManager):
    resource_class = PolicyDefinition
    keyword = 'policy_definition'
    keyword_plural = 'policy_definitions'
    _columns = ["Id", "Name", "Description"]

