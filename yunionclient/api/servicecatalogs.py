from yunionclient.common import base

class Servicecatalog(base.ResourceBase):
    pass


class ServicecatalogManager(base.StandaloneManager):
    resource_class = Servicecatalog
    keyword = 'servicecatalog'
    keyword_plural = 'servicecatalogs'
    _columns = ["Id", "Name", "Public_Scope", "Is_Public", "Icon_Url", "Guest_Template_Id"]

