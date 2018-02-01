from yunionclient.common import base


class BaremetalManager(base.StandaloneManager):
    _columns = ['ID', 'Name', 'Access_MAC', 'Cli_GUID', 'Status', 'Agent_ID',
                'Agent_URI', 'cpu_count', 'mem_size', 'storage_size',
                'HDD', 'SSD', 'SN',
                'Server', 'server_status', 'server_id', 'Enabled',
                'IPMI_IP']
    keyword = 'baremetal'
    keyword_plural = 'baremetals'
