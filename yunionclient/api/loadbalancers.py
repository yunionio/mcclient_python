from yunionclient.common import base


class Loadbalancer(base.ResourceBase):
    pass

class LoadbalancerManager(base.StandaloneManager):
    resource_class = Loadbalancer
    keyword = 'loadbalancer'
    keyword_plural = 'loadbalancers'
    _columns = [
        "id",
        "name",
        "status",
        "address_type",
        "address",
        "network_type",
        "network_id",
        "zone_id",
    ]
    _admin_columns = [
        'tenant',
    ]

class LoadbalancerListener(base.ResourceBase):
    pass


class LoadbalancerListenerManager(base.StandaloneManager):
    resource_class = LoadbalancerListener
    keyword = 'loadbalancerlistener'
    keyword_plural = 'loadbalancerlisteners'
    _columns = [
        "id",
        "name",
        "loadbalancer_id",
        "status",
        "listener_type",
        "listener_port",
        "backend_port",
        "acl_status",
        "acl_type",
    ]
    _admin_columns = [
        'tenant',
    ]

class LoadbalancerListenerRule(base.ResourceBase):
    pass

class LoadbalancerListenerRuleManager(base.StandaloneManager):
    resource_class = LoadbalancerListenerRule
    keyword = 'loadbalancerlistenerrule'
    keyword_plural = 'loadbalancerlistenerrules'
    _columns = [
        "id",
        "name",
        "listener_id",
        "status",
        "domain",
        "path",
        "backend_id",
    ]
    _admin_columns = [
        'tenant',
    ]

class LoadbalancerCertificate(base.ResourceBase):
    pass

class LoadbalancerCertificateManager(base.StandaloneManager):
    resource_class = LoadbalancerCertificate
    keyword = 'loadbalancercertificate'
    keyword_plural = 'loadbalancercertificates'
    _columns = [
        "id",
        "name",
        "algorithm",
        "fingerprint",
        "not_before",
        "not_after",
        "common_name",
        "subject_alternative_names",
    ]
    _admin_columns = [
        'tenant',
    ]

class LoadbalancerBackendGroup(base.ResourceBase):
    pass

class LoadbalancerBackendGroupManager(base.StandaloneManager):
    resource_class = LoadbalancerBackendGroup
    keyword = 'loadbalancerbackendgroup'
    keyword_plural = 'loadbalancerbackendgroups'
    _columns = [
        "id",
        "name",
        "loadbalancer_id",
    ]
    _admin_columns = [
        'tenant',
    ]

class LoadbalancerBackend(base.ResourceBase):
    pass

class LoadbalancerBackendManager(base.StandaloneManager):
    resource_class = LoadbalancerBackend
    keyword = 'loadbalancerbackend'
    keyword_plural = 'loadbalancerbackends'
    _columns = [
        "id",
        "name",
        "backend_group_id",
        "backend_id",
        "backend_type",
        "address",
        "port",
        "weight",
    ]
    _admin_columns = [
        'tenant',
    ]

class LoadbalancerAcl(base.ResourceBase):
    pass

class LoadbalancerAclManager(base.StandaloneManager):
    resource_class = LoadbalancerAcl
    keyword = 'loadbalanceracl'
    keyword_plural = 'loadbalanceracls'
    _columns = [
        "id",
        "name",
        "acl_entries"
    ]
    _admin_columns = [
        'tenant',
    ]

class LoadbalancerCluster(base.ResourceBase):
    pass

class LoadbalancerClusterManager(base.StandaloneManager):
    resource_class = LoadbalancerCluster
    keyword = 'loadbalancercluster'
    keyword_plural = 'loadbalancerclusters'
    _columns = [
        "id",
        "name",
        "zone_id"
    ]

class LoadbalancerAgent(base.ResourceBase):
    pass

class LoadbalancerAgentManager(base.StandaloneManager):
    resource_class = LoadbalancerAgent
    keyword = 'loadbalanceragent'
    keyword_plural = 'loadbalanceragents'
    _columns = [
        "id",
        "name",
        "cluster_id",
        "params",
    ]
