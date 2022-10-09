from yunionclient.common import base

class Sshkeypair(base.ResourceBase):
    pass


class SshkeypairManager(base.StandaloneManager):
    resource_class = Sshkeypair
    keyword = 'sshkeypair'
    keyword_plural = 'sshkeypairs'
    _columns = []