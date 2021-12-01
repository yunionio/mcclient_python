from yunionclient.common import base

class Cachedloadbalancercertificate(base.ResourceBase):
    pass


class CachedloadbalancercertificateManager(base.StandaloneManager):
    resource_class = Cachedloadbalancercertificate
    keyword = 'cachedloadbalancercertificate'
    keyword_plural = 'cachedloadbalancercertificates'
    _columns = ["Id", "Certificate_Id", "Name", "Algorithm", "Fingerprint", "Not_Before", "Not_After", "Common_Name", "Subject_Alternative_Names", "Tenant"]

