from yunionclient.common import base


class SecuritygroupManager(base.StandaloneManager):
    keyword = 'secgroup'
    keyword_plural = 'secgroups'
    _columns = ['ID', 'Name', 'Rules', 'Is_public', 'Created_at', 'Guest_cnt',
                'Description']
