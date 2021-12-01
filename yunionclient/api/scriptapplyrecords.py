from yunionclient.common import base

class Scriptapplyrecord(base.ResourceBase):
    pass


class ScriptapplyrecordManager(base.StandaloneManager):
    resource_class = Scriptapplyrecord
    keyword = 'scriptapplyrecord'
    keyword_plural = 'scriptapplyrecords'
    _columns = ["Script_Id", "Server_Id", "Start_Time", "End_Time", "Reason", "Status"]

