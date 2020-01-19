from yunionclient.common import base
from yunionclient.common import exceptions


class Service(base.ResourceBase):
    pass


class ServiceManager(base.IdentityManager):
    resource_class = Service
    is_admin_api = True
    keyword = 'service'
    keyword_plural = 'services'
    _columns = ['ID', 'Name', 'Type', 'Description']

    def get_by_id_or_name(self, idstr):
        try:
            return self.get(idstr)
        except exceptions.NotFound as e:
            services = self.list()
            for s in services[0]:
                if s['name'] == idstr:
                    return s
            raise e
