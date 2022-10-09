from yunionclient.common import base

class ResResult(base.ResourceBase):
    pass


class ResResultManager(base.MeterManager):
    resource_class = ResResult
    keyword = 'res_result'
    keyword_plural = 'res_results'
    _columns = ["res_id","res_name","cpu","mem","sys_disk","data_disk","ips","res_type","band_width","os_distribution","os_version","platform","region_id","project_name","user_name","start_time","end_time","time_length","cpu_amount","mem_amount","disk_amount","baremetal_amount","gpu_amount","res_fee"]