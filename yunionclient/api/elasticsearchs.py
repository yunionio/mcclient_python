from yunionclient.common import base

class ElasticSearch(base.ResourceBase):
    pass

class ElasticSearchManager(base.StandaloneManager):
    resource_class = ElasticSearch
    keyword = 'elastic_search'
    keyword_plural = "elastic_searchs"
    _columns = ["ID", "Name", "Status", "Zone_id", "Cloudaccount_id", "Vpc_id", "Network_id", "External_id", "Vpc_count", "Vmem_size_gb", "Category", "Instance_type", "Disk_size_gb"]
