
from yunionclient.common import base

class Contact(base.ResourceBase):
    pass


class ContactManager(base.StandaloneManager):
    resource_class = Contact
    keyword = 'contact'
    keyword_plural = 'contacts'
    _columns = []
    _admin_columns = []

