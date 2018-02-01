from yunionclient.common import base


class GroupManager(base.StandaloneManager):
    keyword = 'group'
    keyword_plural = 'groups'
    _columns = ['ID', 'Name', 'Service_type', 'Parent_ID', 'Zone_ID', 'Zone', 'Tenant', 'Sched_Strategy']
