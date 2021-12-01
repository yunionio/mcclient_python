from yunionclient.common import base

class Federatedclusterrole(base.ResourceBase):
    pass


class FederatedclusterroleManager(base.StandaloneManager):
    resource_class = Federatedclusterrole
    keyword = 'federatedclusterrole'
    keyword_plural = 'federatedclusterroles'
    _columns = ["Id", "Name", "Description"]

