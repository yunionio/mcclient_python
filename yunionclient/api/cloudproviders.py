from yunionclient.common import base

class Cloudprovider(base.ResourceBase):
    pass


class CloudproviderManager(base.StandaloneManager):
    resource_class = Cloudprovider
    keyword = 'cloudprovider'
    keyword_plural = 'cloudproviders'
    _columns = ["ID", "Name", "Enabled", "Status", "Access_url", "Account",
                "Sync_Status", "Last_sync", "Last_sync_end_at",
                "health_status",
                "Provider", "guest_count", "host_count", "vpc_count",
                "storage_count", "storage_cache_count", "eip_count",
                "tenant_id", "tenant"
                ]
    _admin_columns = []
