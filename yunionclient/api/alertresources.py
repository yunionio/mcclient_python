from yunionclient.common import base

class Alertresource(base.ResourceBase):
    pass


class AlertresourceManager(base.StandaloneManager):
    resource_class = Alertresource
    keyword = 'alertresource'
    keyword_plural = 'alertresources'
    _columns = ["Id", "Name", "Type", "Count", "Tags"]

