from yunionclient.common import base

class BigqueryOption(base.ResourceBase):
    pass


class BigqueryOptionManager(base.MeterManager):
    resource_class = BigqueryOption
    keyword = 'bigquery_option'
    keyword_plural = 'bigquery_options'
    _columns = ["status"]