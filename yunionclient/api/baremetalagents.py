from yunionclient.common import base


class BaremetalAgentManager(base.StandaloneManager):
    _columns = ['ID', 'Name', 'Access_ip', 'Manager_URI', 'Status']
    keyword = 'baremetalagent'
    keyword_plural = 'baremetalagents'
