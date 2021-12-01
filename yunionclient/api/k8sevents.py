
from yunionclient.common import base

class K8sEvent(base.ResourceBase):
    pass


class K8sEventManager(base.StandaloneManager):
    resource_class = K8sEvent
    keyword = 'k8s_event'
    keyword_plural = 'k8s_events'
    _columns = []
    _admin_columns = []

