from yunionclient.common import base


class AccessGroupCacheManager(base.StandaloneManager):
    keyword = "access_group_cache" 
    keyword_plural = "access_group_caches"
    _columns = []
    _admin_columns = []
