from yunionclient.common import base


class SchedulerManager(base.Manager):

    def schedule(self, **kwargs):
        url = r'/scheduler'
        body = {'scheduler': kwargs}
        resp, body = self.json_request('POST', url, body=body)
        return body['scheduler']
