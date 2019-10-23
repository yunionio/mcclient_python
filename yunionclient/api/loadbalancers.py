from yunionclient.common import base


class LoadbalancerManager(base.StandaloneManager):
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

class LoadbalancerListenerManager(base.StandaloneManager):
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

class LoadbalancerListenerRuleManager(base.StandaloneManager):
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

class LoadbalancerCertificateManager(base.StandaloneManager):
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

class LoadbalancerBackendGroupManager(base.StandaloneManager):
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

class LoadbalancerBackendManager(base.StandaloneManager):
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

class LoadbalancerAclManager(base.StandaloneManager):
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
