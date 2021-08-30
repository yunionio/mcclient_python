from yunionclient.common import base

class Bucket(base.ResourceBase):
    pass


class BucketManager(base.StandaloneManager):
    resource_class = Bucket
    keyword = 'bucket'
    keyword_plural = 'buckets'
    _columns = ["ID", "Name", "Storage_Class",
                "Status", "location", "acl",
                "region", "manager_id", "public_scope",
                ]
    _admin_columns = []
