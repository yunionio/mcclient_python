from yunionclient.common import base

class Filesystem(base.ResourceBase):
    pass


class FilesystemManager(base.StandaloneManager):
    resource_class = Filesystem
    keyword = 'file_system'
    keyword_plural = 'file_systems'
    _columns = ["ID", "Name", "file_system_type",
                "storage_type", "protocol", "capacity",
                "used_capacity", "mount_target_count_limit",
                ]
    _admin_columns = []
