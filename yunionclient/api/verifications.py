
from yunionclient.common import base

class Verification(base.ResourceBase):
    pass


class VerificationManager(base.StandaloneManager):
    resource_class = Verification
    keyword = 'verification'
    keyword_plural = 'verifications'
    _columns = []
    _admin_columns = []

