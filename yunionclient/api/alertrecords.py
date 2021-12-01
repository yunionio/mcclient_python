from yunionclient.common import base

class Alertrecord(base.ResourceBase):
    pass


class AlertrecordManager(base.StandaloneManager):
    resource_class = Alertrecord
    keyword = 'alertrecord'
    keyword_plural = 'alertrecords'
    _columns = ["Id", "Alert_Name", "Res_Type", "Level", "State", "Res_Num", "Eval_Data"]

