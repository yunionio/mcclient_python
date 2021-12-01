from yunionclient.common import base

class SmsConfig(base.ResourceBase):
    pass


class SmsConfigManager(base.StandaloneManager):
    resource_class = SmsConfig
    keyword = 'sms_config'
    keyword_plural = 'sms_configs'
    _columns = ["Type", "Access_Key_Id", "Access_Key_Secret", "Signature", "Sms_Template_One", "Sms_Template_Two", "Sms_Template_Three", "Sms_Check_Code"]

