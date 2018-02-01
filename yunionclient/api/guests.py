from yunionclient.common import base


class GuestManager(base.StandaloneManager):
    keyword = 'server'
    keyword_plural = 'servers'
    _columns = ['ID', 'Name', 'Billing_type', 'IPs', 'Disk', 'Status',
                'vcpu_count', 'vmem_size', 'ext_bw', 'Zone_name', 'Secgroup',
                'Secgrp_id', 'Created_at']
    _admin_columns = ['Host', 'Tenant', 'is_system']
