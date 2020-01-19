import yunionclient

from yunionclient.common import base


class GroupuserManager(base.IdentityJointManager):
    keyword = 'groupuser'
    keyword_plural = 'groupusers'
    _columns = ['Group_ID', 'Group', 'User_ID', 'User']

    @classmethod
    def master_class(cls):
        return yunionclient.api.groups.GroupManager

    @classmethod
    def slave_class(cls):
        return yunionclient.api.users.UserManager
