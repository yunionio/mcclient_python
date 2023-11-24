from yunionclient.common import base

class RoleAssignment(base.ResourceBase):
    pass


class RoleAssignmentManager(base.IdentityManager):
    resource_class = RoleAssignment
    keyword = 'assignment'
    keyword_plural = 'assignments'
    _columns = ["Scope", "User", "Group", "Role", "Policies"]

