from yunionclient.common import base
from yunionclient.common import utils


class BaseResourceSpec(object):

    def __init__(self, brand, region, zone, resourceType, resourceSpec, quantity):
        self.brand = brand
        self.region = region
        self.zone = zone
        self.resourceType = resourceType
        self.resourceSpec = resourceSpec
        self.quantity = quantity

    def get_region(self):
        if self.region is None:
            return ''
        else:
            return self.region

    def get_zone(self):
        if self.zone is None:
            return ''
        else:
            return self.zone

    def price_keys(self):
        val = [self.brand, self.get_region(), self.get_zone(), self.resourceType, self.resourceSpec]
        if self.quantity is not None:
            val.append(self.quantity)
        return '::'.join(val)


class CpuMemSpec(BaseResourceSpec):

    def __init__(self, brand, region, zone, instanceType):
        super(CpuMemSpec, self).__init__(brand, region, zone, "instance", instanceType, None)


class DiskSpec(BaseResourceSpec):

    def __init__(self, brand, region, zone, diskType, sizeGB):
        if type(sizeGB) == int or type(sizeGB) == float:
            if type(sizeGB) == float:
                sizeGB = int(sizeGB)
            sizeGB = '%dGB' % sizeGB
        elif type(sizeGB) == str:
            if not sizeGB.endswith('GB'):
                sizeGB += 'GB'
        else:
            raise Exception('not support size')
        super(DiskSpec, self).__init__(brand, region, zone, "disk", diskType, sizeGB)


class InstanceDiskSpec(object):

    def __init__(self, diskType, sizeGB):
        self.diskType = diskType
        self.sizeGB = sizeGB


class InstanceSpec(object):

    def __init__(self, brand, region, zone, instanceType, diskType, diskSizeGB):
        self.brand = brand
        self.region = region
        self.zone = zone
        self.instanceType = instanceType
        self.disks = [InstanceDiskSpec(diskType, diskSizeGB)]

    def add_disk(self, diskType, diskSizeGB):
        self.disks.append(InstanceDiskSpec(diskType, diskSizeGB))

    def get_specs(self):
        specs = []
        cpu_mem_spec = CpuMemSpec(self.brand, self.region, self.zone, self.instanceType)
        specs.append(cpu_mem_spec)
        for d in self.disks:
            disk_spec = DiskSpec(self.brand, self.region, self.zone, d.diskType, d.sizeGB)
            specs.append(disk_spec)
        return specs


class PriceInfoManager(base.MeterManager):
    keyword = 'price_info'
    keyword_plural = 'price_infos'
    _columns = []

    def get_price(self, specs):
        keys = []
        for spec in specs:
            keys.append(spec.price_keys())
        url = r'/price_infos/total?' + utils.urlencode({'price_keys': keys})
        return self._get(url, self.keyword)
