
from yunionclient.common import base

class IsolatedDevice(base.ResourceBase):
    pass


class IsolatedDeviceManager(base.StandaloneManager):
    resource_class = IsolatedDevice
    keyword = 'isolated_device'
    keyword_plural = 'isolated_devices'
    _columns = []
    _admin_columns = []

