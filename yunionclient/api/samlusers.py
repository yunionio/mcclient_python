from yunionclient.common import base

class Samluser(base.ResourceBase):
    pass


class SamluserManager(base.StandaloneManager):
    resource_class = Samluser
    keyword = 'samluser'
    keyword_plural = 'samlusers'
    _columns = ["Id", "Name", "Description"]

