from yunionclient.common import base

class RoleAssignment(base.ResourceBase):
    pass


class RoleAssignmentManager(base.StandaloneManager):
    resource_class = RoleAssignment
    keyword = 'role_assignment'
    keyword_plural = 'role_assignments'
    _columns = ["Scope", "User", "Group", "Role", "Policies"]

