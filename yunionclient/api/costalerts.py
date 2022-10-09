from yunionclient.common import base

class Costalert(base.ResourceBase):
    pass


class CostalertManager(base.MeterManager):
    resource_class = Costalert
    keyword = 'costalert'
    keyword_plural = 'costalerts'
    _columns = ["brand","account_id","account","cloudprovider_id","cloudprovider_name","region_id","region","domain_id_filter","domain_filter","project_id_filter","project_filter","resource_type","currency","amount","cost_type","user_ids"]