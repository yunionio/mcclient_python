
from yunionclient.common import base

class EmailConfig(base.ResourceBase):
    pass


class EmailConfigManager(base.StandaloneManager):
    resource_class = EmailConfig
    keyword = 'email_config'
    keyword_plural = 'email_configs'
    _columns = []
    _admin_columns = []

