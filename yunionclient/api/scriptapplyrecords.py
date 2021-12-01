
from yunionclient.common import base

class Scriptapplyrecord(base.ResourceBase):
    pass


class ScriptapplyrecordManager(base.StandaloneManager):
    resource_class = Scriptapplyrecord
    keyword = 'scriptapplyrecord'
    keyword_plural = 'scriptapplyrecords'
    _columns = []
    _admin_columns = []

