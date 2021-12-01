from yunionclient.common import base

class Contact(base.ResourceBase):
    pass


class ContactManager(base.StandaloneManager):
    resource_class = Contact
    keyword = 'contact'
    keyword_plural = 'contacts'
    _columns = ["Id", "Name", "Display_Name", "Details", "Status", "Create_By", "Update_By", "Delete_By", "Gmt_Create", "Gmt_Modified", "Gmt_Delete", "Project_Id", "Remark"]

