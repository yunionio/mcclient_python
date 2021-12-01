from yunionclient.common import base

class Verification(base.ResourceBase):
    pass


class VerificationManager(base.StandaloneManager):
    resource_class = Verification
    keyword = 'verification'
    keyword_plural = 'verifications'
    _columns = ["Id", "Cid", "Sent_At", "Expire_At", "Status", "Create_At", "Update_At", "Delete_At", "Create_By", "Update_By", "Delete_By", "Is_Deleted", "Remark"]

