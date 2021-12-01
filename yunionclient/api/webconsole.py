from yunionclient.common import base

class Webconsole(base.ResourceBase):
    pass


class WebconsoleManager(base.StandaloneManager):
    resource_class = Webconsole
    keyword = 'webconsole'
    keyword_plural = 'webconsole'
    _columns = ["Id", "Name", "Description"]

