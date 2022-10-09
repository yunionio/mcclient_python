from yunionclient.common import base

class UnusedResource(base.ResourceBase):
    pass


class UnusedResourceManager(base.MeterManager):
    resource_class = UnusedResource
    keyword = 'unused_resource'
    keyword_plural = 'unused_resources'
    _columns = ["res_id","res_name","res_type","start_time","end_time","project_name","spec","platform","action","quantity","medium_type","storage_type","event_id"]