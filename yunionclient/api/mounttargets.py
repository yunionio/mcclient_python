from yunionclient.common import base

class MountTarget(base.ResourceBase):
    pass

class MountTargetManager(base.StandaloneManager):
    resource_class = MountTarget
    keyword = 'mount_target'
    keyword_plural = "mount_targets"
    _columns = ["Id", "Name", "Network_type", "Vpc", "Domain_name", "File_System_Id"]

