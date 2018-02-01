from yunionclient.common import base


class StorageManager(base.StandaloneManager):
    keyword = 'storage'
    keyword_plural = 'storages'
    _columns = ['ID', 'Name', 'Capacity', 'Status', 'Used_capacity', 'Waste_capacity', 'Free_capacity', 'Storage_type', 'Medium_type', 'Virtual_capacity', 'commit_bound', 'commit_rate']
