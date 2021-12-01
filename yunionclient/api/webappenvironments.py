from yunionclient.common import base

class Webappenvironment(base.ResourceBase):
    pass


class WebappenvironmentManager(base.StandaloneManager):
    resource_class = Webappenvironment
    keyword = 'webappenvironment'
    keyword_plural = 'webappenvironments'
    _columns = ["Id", "Name", "Description"]

