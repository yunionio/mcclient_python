
from yunionclient.common import base

class Release(base.ResourceBase):
    pass


class ReleaseManager(base.StandaloneManager):
    resource_class = Release
    keyword = 'release'
    keyword_plural = 'releases'
    _columns = []
    _admin_columns = []

