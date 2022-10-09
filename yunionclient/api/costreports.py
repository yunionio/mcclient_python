from yunionclient.common import base

class Costreport(base.ResourceBase):
    pass


class CostreportManager(base.MeterManager):
    resource_class = Costreport
    keyword = 'costreport'
    keyword_plural = 'costreports'
    _columns = ["period_type","day","colon_timer","disable","emails","scope","start_run"]