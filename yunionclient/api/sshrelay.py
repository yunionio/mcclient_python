from yunionclient.common import base


class SSHRelayManager(base.Manager):
    service_type = 'sshrelay'

    def get_connections(self):
        resp, body = self.json_request('GET', r'/ssh/connections')
        return body['connections']
