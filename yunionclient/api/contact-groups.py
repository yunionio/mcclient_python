
from yunionclient.common import base

class Contact-group(base.ResourceBase):
    pass


class Contact-groupManager(base.StandaloneManager):
    resource_class = Contact-group
    keyword = 'contact-group'
    keyword_plural = 'contact-groups'
    _columns = []
    _admin_columns = []

