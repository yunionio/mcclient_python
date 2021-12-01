from yunionclient.common import base

class Spec(base.ResourceBase):
    pass


class SpecManager(base.StandaloneManager):
    resource_class = Spec
    keyword = 'spec'
    keyword_plural = 'specs'
    _columns = ["Id", "Name", "Description"]

