from yunionclient.common import base

class MongoDB(base.ResourceBase):
    pass

class MongoDBManager(base.StandaloneManager):
    resource_class = MongoDB
    keyword = 'mongodb'
    keyword_plural = "mongodbs"
    _columns = ["ID", "Name", "Status", "Zone_id", "Cloudaccount_id", "Vpc_id", "Network_id", "External_id", "Vpc_count", "Vmem_size_mb", "Category", "Engine", "Engine_version", "Instance_type", "Disk_size_mb", "Port", "Replication_num", "Ip_addr"]
