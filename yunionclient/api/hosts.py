from yunionclient.common import base


class HostManager(base.StandaloneManager):
    _columns = ['ID', 'Name', 'Access_ip', 'Manager_URI', 'Status', 'Guests',
                    'Running_guests',
                    'storage', 'storage_used', 'storage_virtual',
                    'disk_used', 'storage_free', 'storage_commit_rate',
                    'mem_size', 'mem_used', 'mem_free', 'mem_commit',
                    'cpu_count', 'cpu_used', 'cpu_commit', 'cpu_commit_rate',
                    'mem_commit_rate', 'cpu_commit_bound', 'mem_commit_bound']
    keyword = 'host'
    keyword_plural = 'hosts'
