from yunionclient.common import base

class Guestimage(base.ResourceBase):
    pass


class GuestimageManager(base.StandaloneManager):
    resource_class = Guestimage
    keyword = 'guestimage'
    keyword_plural = 'guestimages'
    _columns = ["Id", "Name", "Status", "Size"]

