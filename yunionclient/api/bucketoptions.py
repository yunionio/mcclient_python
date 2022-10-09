from yunionclient.common import base

class BucketOption(base.ResourceBase):
    pass


class BucketOptionManager(base.MeterManager):
    resource_class = BucketOption
    keyword = 'bucket_option'
    keyword_plural = 'bucket_options'
    _columns = ["status"]