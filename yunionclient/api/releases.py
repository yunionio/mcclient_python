from yunionclient.common import base

class Release(base.ResourceBase):
    pass


class ReleaseManager(base.StandaloneManager):
    resource_class = Release
    keyword = 'release'
    keyword_plural = 'releases'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Namespace_Id", "Namespace", "Labels", "Chart", "Chart_Version", "Type", "Repo_Id", "Repo", "Cluster_Id", "Cluster"]

