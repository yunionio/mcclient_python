import yunionclient
from yunionclient.common import base


class SchedtagManager(base.StandaloneManager):
    keyword = 'schedtag'
    keyword_plural = 'schedtags'
    _columns = ['ID', 'Name', 'Default_strategy']


class SchedtagHostManager(base.JointManager):
    keyword = 'schedtaghost'
    keyword_plural = 'schedtaghosts'
    _columns = ['Schedtag', 'Host', 'Schedtag_ID', 'Host_ID']

    @classmethod
    def master_class(cls):
        return yunionclient.api.schetags.SchedtagManager

    @classmethod
    def slave_class(cls):
        return yunionclient.api.hosts.HostManager
