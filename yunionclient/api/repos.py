
from yunionclient.common import base

class Repo(base.ResourceBase):
    pass


class RepoManager(base.StandaloneManager):
    resource_class = Repo
    keyword = 'repo'
    keyword_plural = 'repos'
    _columns = []
    _admin_columns = []

