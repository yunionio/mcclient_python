from yunionclient.common import base

class IdentityProvider(base.ResourceBase):
    pass


class IdentityProviderManager(base.StandaloneManager):
    resource_class = IdentityProvider
    keyword = 'identity_provider'
    keyword_plural = 'identity_providers'
    _columns = ["Id", "Name", "Driver", "Template", "Auto_Create_User", "Enabled", "Status", "Sync_Status", "Error_Count", "Sync_Interval_Seconds", "Target_Domain_Id"]

