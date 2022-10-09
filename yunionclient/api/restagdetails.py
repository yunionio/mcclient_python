from yunionclient.common import base

class ResTagDetail(base.ResourceBase):
    pass


class ResTagDetailManager(base.MeterManager):
    resource_class = ResTagDetail
    keyword = 'res_tag_detail'
    keyword_plural = 'res_tag_details'
    _columns = ["key","value"]