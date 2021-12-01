from yunionclient.common import base

class Alertrecordshield(base.ResourceBase):
    pass


class AlertrecordshieldManager(base.StandaloneManager):
    resource_class = Alertrecordshield
    keyword = 'alertrecordshield'
    keyword_plural = 'alertrecordshields'
    _columns = ["Id", "Res_Name", "Alert_Name", "Res_Type", "Alert_Id", "Start_Time", "End_Time"]

