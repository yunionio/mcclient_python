from yunionclient.common import base

class Kafka(base.ResourceBase):
    pass

class KafkaManager(base.StandaloneManager):
    resource_class = Kafka
    keyword = 'kafka'
    keyword_plural = "kafkas"
    _columns = ["ID", "Name", "Status", "Version", "Cloudaccount_id", "Vpc_id", "Network_id", "External_id", "Vpc_count", "Vmem_size_mb", "Storage_type"]
