
from yunionclient.common import base

class SmsConfig(base.ResourceBase):
    pass


class SmsConfigManager(base.StandaloneManager):
    resource_class = SmsConfig
    keyword = 'sms_config'
    keyword_plural = 'sms_configs'
    _columns = []
    _admin_columns = []

