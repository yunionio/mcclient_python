from yunionclient.common import base

class CapabilityManager(base.StandaloneManager):
    keyword = "capability" 
    keyword_plural = "capabilities"
    _columns = []
    _admin_columns = []

    def list(self, **kwargs):
        url = r'/capabilities'
        if len(kwargs) > 0:
            url += '?' + utils.urlencode(kwargs)
        return self._get(url, "")

