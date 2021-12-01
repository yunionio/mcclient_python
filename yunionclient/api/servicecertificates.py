from yunionclient.common import base

class Servicecertificate(base.ResourceBase):
    pass


class ServicecertificateManager(base.StandaloneManager):
    resource_class = Servicecertificate
    keyword = 'servicecertificate'
    keyword_plural = 'servicecertificates'
    _columns = ["Id", "Name", "Algorithm", "Fingerprint", "Not_Before", "Not_After", "Common_Name", "Subject_Alternative_Names", "Tenant"]

