from yunionclient.common import base

class GroupManager(base.IdentityManager):
    is_admin_api = True
    keyword = 'group'
    keyword_plural = 'groups'
    _columns = ['ID', 'Name', 'Displayname']
