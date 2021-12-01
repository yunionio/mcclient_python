from yunionclient.common import base

class IsolatedDevice(base.ResourceBase):
    pass


class IsolatedDeviceManager(base.StandaloneManager):
    resource_class = IsolatedDevice
    keyword = 'isolated_device'
    keyword_plural = 'isolated_devices'
    _columns = ["Id", "Dev_Type", "Model", "Addr", "Vendor_Device_Id", "Host_Id", "Host", "Guest_Id", "Guest", "Guest_Status"]

