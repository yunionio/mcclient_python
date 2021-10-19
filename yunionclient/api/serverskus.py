from yunionclient.common import base

class ServerSku(base.ResourceBase):
    pass


class ServerSkuManager(base.StandaloneManager):
    resource_class = ServerSku
    keyword = 'serversku'
    keyword_plural = 'serverskus'
    _columns = ['ID', 'Name', 'Instance_type_family', 
            'Instance_type_category', 'Cpu_core_count', 'Memory_size_mb',
            'Os_name', 'Sys_disk_resizable', 'Attached_disk_type', 'Attached_disk_size_gb',
            'Attached_disk_count', 'Data_disk_types', 'Data_disk_max_count', 'Nic_max_count',
            'Cloudregion_id', 'Provider', 'Postpaid_status', 'Prepaid_status', 'Created_at']
    _admin_columns = []
