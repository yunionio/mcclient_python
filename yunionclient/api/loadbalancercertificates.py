from yunionclient.common import base

class Loadbalancercertificate(base.ResourceBase):
    pass


class LoadbalancercertificateManager(base.StandaloneManager):
    resource_class = Loadbalancercertificate
    keyword = 'loadbalancercertificate'
    keyword_plural = 'loadbalancercertificates'
    _columns = ["Id", "Name", "Algorithm", "Fingerprint", "Not_Before", "Not_After", "Common_Name", "Subject_Alternative_Names", "Tenant"]

