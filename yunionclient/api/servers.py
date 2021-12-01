
from yunionclient.common import base

class Server(base.ResourceBase):
    pass


class ServerManager(base.StandaloneManager):
    resource_class = Server
    keyword = 'server'
    keyword_plural = 'servers'
    _columns = []
    _admin_columns = []

