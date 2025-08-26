from yunionclient.common import base

class Receiver(base.ResourceBase):
    pass


class ReceiverManager(base.NotifyManager):
    resource_class = Receiver
    keyword = 'receiver'
    keyword_plural = 'receivers'
    _columns = ["Id", "Name", "Domain_Id", "Project_Domain", "Email", "International_Mobile", "Enabled_Contact_Types", "Verified_Infos"]

