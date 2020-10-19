from yunionclient.common import base


class Network(base.ResourceBase):
    pass


class NetworkManager(base.StandaloneManager):
    resource_class = Network
    keyword = 'network'
    keyword_plural = 'networks'
    _columns = ['ID', 'Name', 'Guest_ip_start', 'Guest_ip_end', 'Guest_ip_mask',
                    'wire_id', 'wire', 'is_public', 'exit', 'Ports', 'vnics',
                    'group_vnics', 'bm_vnics', 'reserve_vnics', 'server_type']
