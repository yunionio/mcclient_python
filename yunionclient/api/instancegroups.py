from yunionclient.common import base

class Instancegroup(base.ResourceBase):
    pass


class InstancegroupManager(base.StandaloneManager):
    resource_class = Instancegroup
    keyword = 'instancegroup'
    keyword_plural = 'instancegroups'
    _columns = ["Id", "Name", "Service_Type", "Parent_Id", "Zone_Id", "Sched_Strategy", "Domain_Id", "Project_Id", "Granularity", "Is_Froced_Sep"]

