
from yunionclient.common import base

class Scheudledtaskactivity(base.ResourceBase):
    pass


class ScheudledtaskactivityManager(base.StandaloneManager):
    resource_class = Scheudledtaskactivity
    keyword = 'scheudledtaskactivity'
    keyword_plural = 'scheduledtaskactivities'
    _columns = []
    _admin_columns = []

