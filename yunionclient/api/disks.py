from yunionclient.common import base


class DiskManager(base.StandaloneManager):
    keyword = 'disk'
    keyword_plural = 'disks'
    _columns = ['ID', 'Name', 'Billing_type', 'Disk_size', 'Status', 'Disk_format', 'Is_public',
                    'Guest_count', 'Storage_type']
    _admin_columns = ['Storage', 'Tenant']
