from yunionclient.common import base

class Secret(base.ResourceBase):
    pass


class SecretManager(base.StandaloneManager):
    resource_class = Secret
    keyword = 'secret'
    keyword_plural = 'secrets'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Namespace_Id", "Namespace", "Labels", "Type", "Cluster_Id", "Cluster"]

