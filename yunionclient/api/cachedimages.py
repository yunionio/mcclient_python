from yunionclient.common import base


class CachedimageManager(base.StandaloneManager):
    keyword = 'cachedimage'
    keyword_plural = 'cachedimages'
    _columns = ['ID', 'Name', 'Bandwidth', 'Region', 'Provider']
