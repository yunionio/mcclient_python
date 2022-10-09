from yunionclient.common import base

class Dynamicschedtag(base.ResourceBase):
    pass


class DynamicschedtagManager(base.StandaloneManager):
    resource_class = Dynamicschedtag
    keyword = 'dynamicschedtag'
    keyword_plural = 'dynamicschedtags'
    _columns = ["ID","Name","Description","Condition","Schedtag","Schedtag_Id","Resource_Type","Enabled"]