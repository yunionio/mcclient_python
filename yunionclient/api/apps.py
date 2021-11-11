from yunionclient.common import base

class AppManager(base.StandaloneManager):
    keyword = "webapp" 
    keyword_plural = "webapps"
    _columns = []
    _admin_columns = []
