from yunionclient.common import base

from .users import User


class Project(base.ResourceBase):
    pass


class ProjectManager(base.IdentityManager):
    resource_class = Project
    is_admin_api = True
    keyword = 'project'
    keyword_plural = 'projects'
    _columns = ['ID', 'Name', 'Enabled', 'Domain_Id', 'Parent_Id']

    def list_users(self, tid):
        url = r'/projects/%s/users' % tid
        return self._list(url, 'users', obj_class=User)
