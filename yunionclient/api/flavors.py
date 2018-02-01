from yunionclient.common import base


class FlavorManager(base.StandaloneManager):
    keyword = 'flavor'
    keyword_plural = 'flavors'
    _columns = ['ID', 'Name', 'VCPU_count', 'VMEM_size', 'Disk_size',
                'Disk_backend', 'Ext_Bandwidth', 'Int_Bandwidth', 'is_public',
                'Description', 'Aggregate_strategy', 'Flavor_type']
