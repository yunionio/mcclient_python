from yunionclient.common import base

class DnsRecordset(base.ResourceBase):
    pass


class DnsRecordsetManager(base.StandaloneManager):
    resource_class = DnsRecordset
    keyword = "dns_recordset" 
    keyword_plural = "dns_recordsets"
    _columns = []
    _admin_columns = []
