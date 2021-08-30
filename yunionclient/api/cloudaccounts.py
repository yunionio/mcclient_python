from yunionclient.common import base

class Cloudaccount(base.ResourceBase):
    pass


class CloudaccountManager(base.StandaloneManager):
    resource_class = Cloudaccount
    keyword = 'cloudaccount'
    keyword_plural = 'cloudaccounts'
    _columns = ["ID", "Name", "Enabled", "Status", "Access_url",
                "balance", "error_count", "health_status",
                "Sync_Status", "Last_sync",
                "guest_count", "project_domain", "domain_id",
                "Provider", "Brand",
                "Enable_Auto_Sync", "Sync_Interval_Seconds",
                "Share_Mode", "is_public", "public_scope",
                "auto_create_project",
                ]
    _admin_columns = []
