from yunionclient.common import base

class Parameter(base.ResourceBase):
    pass


class ParameterManager(base.StandaloneManager):
    resource_class = Parameter
    keyword = 'parameter'
    keyword_plural = 'parameters'
    _columns = ["Id", "Created_At", "Update_At", "Name", "Value", "Namespace", "Namespace_Id", "Created_By", "Updated_By"]

