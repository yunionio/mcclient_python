from yunionclient.common import base

class Webconsole(base.ResourceBase):
    pass


class WebconsoleManager(base.WebconsoleManager):
    resource_class = Webconsole
    keyword = 'webconsole'
    keyword_plural = 'webconsole'
    _columns = ["Id", "Name", "Description"]

    def do_connect(self, res_type, id, action, **kwargs):
        url = r'/webconsole/' + res_type
        if id != '':
            url += '/' + id
        if action != '':
            url += '/' + action
        return self._create(url, kwargs, 'webconsole')

    def do_server_connect(self, id, **kwargs):
        info = self.do_connect('server', id, '', **kwargs)
        return '/web-console/no-vnc?data=' + info.connect_params
