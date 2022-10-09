from yunionclient.common import base

class ResourceDetail(base.ResourceBase):
    pass


class ResourceDetailManager(base.MeterManager):
    resource_class = ResourceDetail
    keyword = 'resource_detail'
    keyword_plural = 'resource_details'
    _columns = ["res_type","res_id","res_name","start_time","end_time","project_name","user_name","res_fee"]