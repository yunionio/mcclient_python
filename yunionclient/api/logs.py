from yunionclient.common import base


class LogManager(base.StandaloneManager):
    _columns = ['id', 'ops_time', 'obj_id', 'obj_type', 'obj_name', 'action', 'notes']
    keyword = 'event'
    keyword_plural = 'events'
