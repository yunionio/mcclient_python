import sys

import yunionclient

from yunionclient.common import utils

import json


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
@utils.arg('--flavor-type', metavar='<FLVAOR_TYPE>', help='Flavor type', choices=['server', 'rds'])
def do_flavor_list(client, args):
    """List flavors."""
    page_info = utils.get_paging_info(args)
    if args.flavor_type:
        page_info['flavor_type'] = args.flavor_type
    flavors = client.flavors.list(**page_info)
    utils.print_list(flavors, client.flavors.columns)


@utils.arg('name', metavar='<FLAVOR_NAME>', help='Name of flavor to be created')
@utils.arg('--cpu', metavar='<VCPU_COUNT>', required=True, help='Count of virtual CPU cores')
@utils.arg('--mem', metavar='<VMEM_SIZE>', required=True, help='Size of memory, default in MB')
@utils.arg('--disk', metavar='<DATA_DISK_SIZE>', help='Data disk size, default in GB')
@utils.arg('--disk-backend', metavar='<DISK_BACKEND>', choices=['local', 'baremetal', 'mebs', 'ceph', 'sheepdog'], help='Disk backend')
@utils.arg('--ext-bw', metavar='<BANDWIDTH>', help='Bandwidth limit for exit network interface')
@utils.arg('--int-bw', metavar='<BANDWIDTH>', help='Bandwidth limit for internal network interface')
@utils.arg('--public', action='store_true', help='Is flavor publicly available')
@utils.arg('--desc', metavar='<FLAVOR_DESC>', help='Short description of flavor')
@utils.arg('--aggregate', metavar='<KEY:VALUE>', action='append', help='Schedule policy, key = aggregate name, value = require|exclude|prefer|avoid')
@utils.arg('--flavor-type', metavar='<FLVAOR_TYPE>', help='Flavor type', choices=['server', 'rds'])
def do_flavor_create(client, args):
    """ Create a flavor """
    kwargs = {}
    kwargs['name'] = args.name
    kwargs['vcpu_count'] = int(args.cpu)
    kwargs['vmem_size'] = args.mem
    if args.disk:
        kwargs['disk_size'] = args.disk
    if args.disk_backend:
        kwargs['disk_backend'] = args.disk_backend
    if args.ext_bw:
        kwargs['ext_bandwidth'] = args.ext_bw
    if args.int_bw:
        kwargs['int_bandwidth'] = args.int_bw
    if args.public:
        kwargs['is_public'] = True
    else:
        kwargs['is_public'] = False
    if args.desc:
        kwargs['description'] = args.desc
    if args.aggregate:
        index = 0
        for aggregate in args.aggregate:
            if len(aggregate.split(':')) == 2:
                kwargs['aggregate.%d' % index] = aggregate
                index += 1
            else:
                print('Aggregate format error: %s' % aggregate)
                return
    if args.flavor_type:
        kwargs['flavor_type'] = args.flavor_type
    flavor = client.flavors.create(**kwargs)
    utils.print_dict(flavor)


@utils.arg('id', metavar='<FLAVOR_ID>', help='ID or unique name of flavor to be updated')
@utils.arg('--name', metavar='<FLAVOR_NAME>', help='New name of flavor')
@utils.arg('--desc', metavar='<FLAVOR_DESC>', help='Short description of flavor')
@utils.arg('--cpu', metavar='<VCPU_COUNT>', help='Count of virtual CPU cores')
@utils.arg('--mem', metavar='<VMEM_SIZE>', help='Size of memory, default in MB')
@utils.arg('--disk', metavar='<DATA_DISK_SIZE>', help='Data disk size, default in GB')
@utils.arg('--disk-backend', metavar='<DISK_BACKEND>', choices=['local', 'baremetal', 'mebs', 'ceph', 'sheepdog'], help='Disk backend')
@utils.arg('--ext-bw', metavar='<BANDWIDTH>', help='Bandwidth limit for exit network interface')
@utils.arg('--int-bw', metavar='<BANDWIDTH>', help='Bandwidth limit for internal network interface')
@utils.arg('--aggregate', metavar='<KEY:VALUE>', action='append', help='Schedule policy, key = aggregate name, value = require|exclude|prefer|avoid')
@utils.arg('--flavor-type', metavar='<FLVAOR_TYPE>', help='Flavor type', choices=['server', 'rds'])
@utils.arg('--aggregate-clear', action='store_true', help='Clear aggregate')
def do_flavor_update(client, args):
    """ Update a flavor """
    kwargs = {}
    if args.name:
        kwargs['name'] = args.name
    if args.cpu:
        kwargs['vcpu_count'] = int(args.cpu)
    if args.mem:
        kwargs['vmem_size'] = args.mem
    if args.disk:
        kwargs['disk_size'] = args.disk
    if args.disk_backend:
        kwargs['disk_backend'] = args.disk_backend
    if args.ext_bw:
        kwargs['ext_bandwidth'] = args.ext_bw
    if args.int_bw:
        kwargs['int_bandwidth'] = args.int_bw
    if args.desc:
        kwargs['description'] = args.desc
    if args.aggregate_clear:
        kwargs['aggregate_clear'] = True
    if args.aggregate:
        index = 0
        for aggregate in args.aggregate:
            if len(aggregate.split(':')) == 2:
                kwargs['aggregate.%d' % index] = aggregate
                index += 1
            else:
                print('Aggregate format error: %s' % aggregate)
                return
    if args.flavor_type:
        kwargs['flavor_type'] = args.flavor_type

    if len(kwargs) == 0:
        raise Exception('No data to update')
    flavor = client.flavors.update(args.id, **kwargs)
    utils.print_dict(flavor)


@utils.arg('id', metavar='<FLAVOR_ID>', help='ID or unique name of flavor to be updated')
def do_flavor_delete(client, args):
    """ Delete a flavor """
    flavor = client.flavors.delete(args.id)
    utils.print_dict(flavor)


@utils.arg('id', metavar='<FLAVOR_ID>', help='ID or unique name of flavor to get')
def do_flavor_show(client, args):
    """ Show details of a flavor """
    flavor = client.flavors.get(args.id)
    utils.print_dict(flavor)


@utils.arg('id', metavar='<FLAVOR_ID>', help='ID of flavor to make public')
def do_flavor_public(client, args):
    """ Make a flavor public """
    flavor = client.flavors.perform_action(args.id, 'public')
    utils.print_dict(flavor)


@utils.arg('id', metavar='<FLAVOR_ID>', help='ID of flavor to make private')
def do_flavor_private(client, args):
    """ Make a flavor private """
    flavor = client.flavors.perform_action(args.id, 'private')
    utils.print_dict(flavor)


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--admin', action='store_true', help='Is administrative Call?')
@utils.arg('--user', metavar='<USER>', help='Filter results by user id in admin mode')
def do_keypair_list(client, args):
    """List keypairs."""
    page_info = utils.get_paging_info(args)
    keypairs = client.keypairs.list(**page_info)
    utils.print_list(keypairs, client.keypairs.columns)


@utils.arg('name', metavar='<KEYPAIR_NAME>', help='Name of keypair to be created')
@utils.arg('--scheme', metavar='<SCHEME>', choices=['RSA', 'DSA'], default='RSA', help='Scheme of keypair, RSA or DSA, default is RSA')
@utils.arg('--desc', metavar='<KEYPAIR_DESC>', help='Short description of keypair')
def do_keypair_create(client, args):
    """ Create a new keypair """
    kwargs = {}
    kwargs['name'] = args.name
    if args.desc is not None:
        kwargs['description'] = args.desc
    if args.scheme is not None:
        kwargs['scheme'] = args.scheme
    keypair = client.keypairs.create(**kwargs)
    utils.print_dict(keypair)


@utils.arg('id', metavar='<KEYPAIR_ID>', help='ID to be deleted')
@utils.arg('--name', metavar='<KEYPAIR_NAME>', help='Name of keypair to be created')
@utils.arg('--desc', metavar='<KEYPAIR_DESC>', help='Short description of keypair')
def do_keypair_update(client, args):
    """ Create a new keypair """
    kwargs = {}
    kwargs['id'] = args.id
    if args.name is not None:
        kwargs['name'] = args.name
    if args.desc is not None:
        kwargs['description'] = args.desc

    keypair = client.keypairs.update(args.id, **kwargs)
    utils.print_dict(keypair)

@utils.arg('id', metavar='<KEYPAIR_ID>', help='ID to be deleted')
def do_keypair_delete(client, args):
    """ Delete keypair of id """
    deled = client.keypairs.delete(args.id)
    utils.print_dict(deled)


@utils.arg('id', metavar='<KEYPAIR_ID>', help='ID to be shown')
def do_keypair_show(client, args):
    """ show details of a keypair """
    kp = client.keypairs.get(args.id)
    utils.print_dict(kp)


@utils.arg('id', metavar='<KEYPAIR_ID>', help='ID of keypair to fetch')
def do_keypair_privatekey(client, args):
    """ Fetch the private key of a keypair, this can be done once only """
    kp = client.keypairs.get_specific(args.id, 'privatekey')
    if isinstance(kp, dict):
        prikey = kp.get('private_key', None)
    else:
        prikey = getattr(kp, 'private_key', None)
    if prikey is not None:
        print(prikey)
    else:
        print("Key has been fetched")


@utils.arg('name', metavar='<KEYPAIR_NAME>', help='Name of keypair to be created')
@utils.arg('--desc', metavar='<KEYPAIR_DESC>', help='Short description of keypair')
@utils.arg('--public-key', metavar='<PUBLIC_KEY_FILENAME>', help='Filename of public key file, or public key can be supplied via stdin')
def do_keypair_import(client, args):
    """
    Create a new keypair with a existing public key
    The public key can be provided in a file specified by --public-key option
    Or can be read from stdin
    """
    kwargs = {}
    kwargs['name'] = args.name
    if args.desc is not None:
        kwargs['description'] = args.desc

    pubkey = None
    if args.public_key is not None:
        with open(args.public_key) as pf:
            pubkey = pf.read()
    else:
        pubkey = sys.stdin.read()
    if pubkey is not None:
        kwargs['public_key'] = pubkey
        keypair = client.keypairs.create(**kwargs)
        utils.print_dict(keypair)
    else:
        raise Exception("No public key provided")


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_zone_list(client, args):
    """List zones."""
    page_info = utils.get_paging_info(args)
    zones = client.zones.list(**page_info)
    utils.print_list(zones, client.zones.columns)


@utils.arg('id', metavar='<ZONE_ID>', help='ID or Name of Zone to describe.')
@utils.arg('--with-meta', action='store_true', help='With meta data')
def do_zone_show(client, args):
    """Describe a specific zone."""
    kwargs = {}
    if args.with_meta:
        kwargs['with_meta'] = True

    zone = client.zones.get(args.id, **kwargs)
    utils.print_dict(zone)


@utils.arg('name', metavar='<ZONE_NAME>', help='Name of Zone.')
@utils.arg('--name-cn', metavar='<ZONE_CN_NAME>', help='Name of zone.')
@utils.arg('--location', metavar='<ZONE_LOCATION>', help='Location of Zone.')
@utils.arg('--contacts', metavar='<ZONE_CONTACTS>', help='Contact person of Zone.')
@utils.arg('--manager-uri', metavar='<ZONE_MANAGER_URI>', help='Zone manager URI')
@utils.arg('--status', metavar='<ZONE_STATUS>', choices=['enable', 'disable', 'soldout', 'lack'], default='disable')
@utils.arg('--desc', metavar='<ZONE_DESC>', help='Description of zone')
def do_zone_create(client, args):
    """ Create a new zone. """
    kwargs = {}
    kwargs['name'] = args.name
    if args.location is not None:
        kwargs['location'] = args.location
    if args.contacts is not None:
        kwargs['contacts'] = args.contacts
    if args.desc is not None:
        kwargs['description'] = args.desc
    if args.manager_uri is not None:
        kwargs['manager_uri'] = args.manager_uri
    if args.name_cn is not None:
        kwargs['name_cn'] = args.name_cn
    if args.status is not None:
        kwargs['status'] = args.status
    zone = client.zones.create(**kwargs)
    utils.print_dict(zone)


@utils.arg('id', metavar='<ZONE_ID>', help='ID of Zone to delete.')
def do_zone_delete(client, args):
    """ delete a zone """
    zone = client.zones.delete(args.id)
    utils.print_dict(zone)


@utils.arg('id', metavar='<ZONE_ID>', help='ID of Zone')
@utils.arg('--ssd', metavar='<SSDSUPPORT>', choices=['on', 'off'], help='If support ssd')
def do_zone_update_metadata(client, args):
    """ update zone metadata """
    kwargs = {}
    if args.ssd:
        kwargs['ssd'] = args.ssd
    zone = client.zones.perform_action(args.id, 'metadata', **kwargs)
    utils.print_dict(zone)


@utils.arg('id', metavar='<ZONE_ID>', help='ID of Zone to update')
@utils.arg('--name', metavar='<ZONE_NAME>', help='Name of zone')
@utils.arg('--name-cn', metavar='<ZONE_CN_NAME>', help='Name of zone.')
@utils.arg('--desc', metavar='<ZONE_DESC>', help='Description of zone')
@utils.arg('--location', metavar='<ZONE_LOCATION>', help='Location of zone')
@utils.arg('--contacts', metavar='<ZONE_CONTACTS>', help='Contacts of zone')
@utils.arg('--manager-uri', metavar='ZONE_MANAGER_URI>', help='Zone manager URI')
@utils.arg('--admin-id', metavar='<ADMIN_TENANT_ID>', help='Admin tenant ID')
@utils.arg('--status', metavar='<ZONE_STATUS>', choices=['enable', 'disable', 'soldout', 'lack'])
def do_zone_update(client, args):
    """ Update a zone """
    kwargs = {}
    if args.name is not None:
        kwargs['name'] = args.name
    if args.desc is not None:
        kwargs['description'] = args.desc
    if args.location is not None:
        kwargs['location'] = args.location
    if args.contacts is not None:
        kwargs['contacts'] = args.contacts
    if args.admin_id is not None:
        kwargs['admin_id'] = args.admin_id
    if args.manager_uri is not None:
        kwargs['manager_uri'] = args.manager_uri
    if args.name_cn is not None:
        kwargs['name_cn'] = args.name_cn
    if args.status is not None:
        kwargs['status'] = args.status

    if len(kwargs) == 0:
        raise Exception("Nothing to update")
    zone = client.zones.update(args.id, **kwargs)
    utils.print_dict(zone)


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_cluster_list(client, args):
    """ List clusters """
    page_info = utils.get_paging_info(args)
    clusters = client.clusters.list(**page_info)
    utils.print_list(clusters, client.clusters.columns)


@utils.arg("id", metavar="<ZONE_ID>", help='ID of zones to inspect')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_zone_list_cluster(client, args):
    """ List clusters in a zone """
    page_info = utils.get_paging_info(args)
    clusters = client.zones.list_descendent(args.id,
            yunionclient.api.clusters.ClusterManager, **page_info)
    utils.print_list(clusters, client.clusters.columns)


@utils.arg('id', metavar='<ZONE_ID>', help='ID of zone of cluster')
@utils.arg('--name', metavar='<CLUSTER_NAME>', required=True, help='Name of cluster to create')
@utils.arg('--start-ip', metavar='<START_IP>', required=True, help='Start ip address of hosts in cluster')
@utils.arg('--end-ip', metavar='<END_IP>', required=True, help='End ip address of hosts in cluster')
@utils.arg('--desc', metavar='<CLUSTER_DESC>', help='Description of cluster')
@utils.arg('--netmask', metavar='<NETMASK_LEN>', help='Length of netmask')
@utils.arg('--gateway', metavar='<GATEWAY>', help='Gateway of cluster')
@utils.arg('--dns', metavar='<DNS_SERVER>', help='DNS server of cluster')
def do_zone_create_cluster(client, args):
    """ Create a cluster inside a zone """
    kwargs = {}
    kwargs['name'] = args.name
    kwargs['host_ip_start'] = args.start_ip
    kwargs['host_ip_end'] = args.end_ip
    if args.desc is not None:
        kwargs['description'] = args.desc
    if args.netmask is not None:
        kwargs['host_netmask'] = args.netmask
    if args.gateway is not None:
        kwargs['host_gateway'] = args.gateway
    if args.dns is not None:
        kwargs['host_dns'] = args.dns
    cluster = client.zones.create_descendent(args.id,
                    yunionclient.api.clusters.ClusterManager, **kwargs)
    utils.print_dict(cluster)


#@utils.arg('name', metavar='<CLUSTER_NAME>', help='Name of cluster to create')
#@utils.arg('--zone-id', metavar='<ZONE_ID>', required=True, help='ID of zone of cluster')
#@utils.arg('--desc', metavar='<CLUSTER_DESC>', help='Description of cluster')
#@utils.arg('--start-ip', metavar='<START_IP>', required=True, help='Start ip address of hosts in cluster')
#@utils.arg('--end-ip', metavar='<END_IP>', required=True, help='End ip address of hosts in cluster')
#@utils.arg('--netmask', metavar='<NETMASK_LEN>', help='Length of netmask')
#@utils.arg('--gateway', metavar='<GATEWAY>', help='Gateway of cluster')
#@utils.arg('--dns', metavar='<DNS_SERVER>', help='DNS server of cluster')
#def do_cluster_create(client, args):
#    """ Create new cluster """
#    try:
#        kwargs = {}
#        if args.zone_id is None or len(args.zone_id) == 0:
#            raise "Zone ID must present"
#        kwargs['name'] = args.name
#        kwargs['zone_id'] = args.zone_id
#        kwargs['host_ip_start'] = args.start_ip
#        kwargs['host_ip_end'] = args.end_ip
#        if args.desc is not None:
#            kwargs['description'] = args.desc
#        if args.netmask is not None:
#            kwargs['host_netmask'] = args.netmask
#        if args.gateway is not None:
#            kwargs['host_gateway'] = args.gateway
#        if args.dns is not None:
#            kwargs['host_dns'] = args.dns
#        cluster = client.clusters.create(**kwargs)
#        utils.print_dict(cluster)
#    except Exception as e:
#        utils.show_exception_and_exit(e)


@utils.arg('id', metavar='<CLUSTER_ID>', help='ID of cluster to show')
def do_cluster_show(client, args):
    """ Show details of client """
    cluster = client.clusters.get(args.id)
    utils.print_dict(cluster)


@utils.arg('id', metavar='<CLUSTER_ID>', help='ID of cluster to delete')
def do_cluster_delete(client, args):
    """ Delete cluster """
    cluster = client.clusters.delete(args.id)
    utils.print_dict(cluster)


@utils.arg('id', metavar='<CLUSTER_ID>', help='ID of cluster to update')
@utils.arg('--name', metavar='<CLUSTER_NAME>', help='Name of cluster')
@utils.arg('--desc', metavar='<CLUSTER_DESC>', help='Description of cluster')
@utils.arg('--start-ip', metavar='<START_IP>', help='Start ip address of hosts in cluster')
@utils.arg('--end-ip', metavar='<END_IP>', help='End ip address of hosts in cluster')
@utils.arg('--netmask', metavar='<NETMASK_LEN>', help='Length of netmask')
@utils.arg('--gateway', metavar='<GATEWAY>', help='Gateway of cluster')
@utils.arg('--dns', metavar='<DNS_SERVER>', help='DNS server of cluster')
def do_cluster_update(client, args):
    """ Update cluster """
    kwargs = {}
    if args.name is not None:
        kwargs['name'] = args.name
    #if args.zone_id is not None:
    #    kwargs['zone_id'] = args.zone_id
    if args.desc is not None:
        kwargs['description'] = args.desc
    if args.start_ip is not None:
        kwargs['host_ip_start'] = args.start_ip
    if args.end_ip is not None:
        kwargs['host_ip_end'] = args.end_ip
    if args.netmask is not None:
        kwargs['host_netmask'] = args.netmask
    if args.gateway is not None:
        kwargs['host_gateway'] = args.gateway
    if args.dns is not None:
        kwargs['host_dns'] = args.dns
    cluster = client.clusters.update(args.id, **kwargs)
    utils.print_dict(cluster)


@utils.arg('id', metavar='<CLUSTER_ID>', help='ID of cluster to update')
def do_cluster_update_schedule_rank(client, args):
    cluster = client.clusters.perform_action(args.id, 'update_schedule_rank')
    utils.print_dict(cluster)


@utils.arg('id', metavar='<CLUSTER_ID>', help='ID of host cluster')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_cluster_list_host(client, args):
    """ List hosts in a cluster """
    page_info = utils.get_paging_info(args)
    hosts = client.clusters.list_descendent(args.id,
                    yunionclient.api.hosts.HostManager, **page_info)
    utils.print_list(hosts, client.hosts.columns)


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_host_list(client, args):
    """ List hosts """
    page_info = utils.get_paging_info(args)
    hosts = client.hosts.list(**page_info)
    utils.print_list(hosts, client.hosts.columns)


@utils.arg('id', metavar='<CLUSTER_ID>', help='ID of host cluster')
@utils.arg('--name', metavar='<HOST_NAME>', required=True, help='Name of host')
@utils.arg('--ip', metavar='<ACCESS_IP>', required=True, help='Access IP of host')
@utils.arg('--memory', metavar='<HOST_MEMORY>', help='Memory in MB')
@utils.arg('--manager-uri', metavar='<HOST_MANAGER_URI>', help='Access URI of this host')
@utils.arg('--desc', metavar='<HOST_DESC>', help='Description of host')
@utils.arg('--rack', metavar='<HOST_RACK>', help='Rack NO of host')
@utils.arg('--slot', metavar='<HOST_SLOT>', help='Slot NO of host')
@utils.arg('--cpu-count', metavar='<HOST_CPU_COUNT>', help='Number of CPU cores')
@utils.arg('--cpu-mhz', metavar='<HOST_CPU_HZ>', help='Frequency of CPU')
def do_cluster_create_host(client, args):
    """ Create a host in a cluster """
    kwargs = {}
    kwargs['name'] = args.name
    kwargs['access_ip'] = args.ip
    if args.manager_uri is not None:
        kwargs['manager_uri'] = args.manager_uri
    if args.desc is not None:
        kwargs['description'] = args.desc
    if args.rack is not None:
        kwargs['rack'] = args.rack
    if args.slot is not None:
        kwargs['slots'] = args.slot
    if args.cpu_count is not None:
        kwargs['cpu_count'] = args.cpu_count
    if args.cpu_mhz is not None:
        kwargs['cpu_mhz'] = args.cpu_mhz
    if args.memory is not None:
        kwargs['mem_size'] = args.memory
    host = client.clusters.create_descendent(args.id,
                    yunionclient.api.hosts.HostManager, **kwargs)
    utils.print_dict(host)


#@utils.arg('name', metavar='<HOST_NAME>', help='Name of host')
#@utils.arg('--cluster-id', metavar='<CLUSTER_ID>', required=True, help='ID of host cluster')
#@utils.arg('--ip', metavar='<ACCESS_IP>', required=True, help='Access IP of host')
#@utils.arg('--memory', metavar='<HOST_MEMORY>', help='Memory in MB')
#@utils.arg('--manager-uri', metavar='<ACCESS_IP>', help='Access URI of this host')
#@utils.arg('--desc', metavar='<HOST_DESC>', help='Description of host')
#@utils.arg('--rack', metavar='<HOST_RACK>', help='Rack NO of host')
#@utils.arg('--slot', metavar='<HOST_SLOT>', help='Slot NO of host')
#@utils.arg('--cpu-count', metavar='<HOST_CPU_COUNT>', help='Number of CPU cores')
#@utils.arg('--cpu-mhz', metavar='<HOST_CPU_HZ>', help='Frequency of CPU')
#def do_host_create(client, args):
#    """ Create a host """
#    try:
#        kwargs = {}
#        kwargs['name'] = args.name
#        kwargs['cluster_id'] = args.cluster_id
#        kwargs['access_ip'] = args.ip
#        if args.manager_uri is not None:
#            kwargs['manager_uri']  = args.manager_uri
#        if args.desc is not None:
#            kwargs['description'] = args.desc
#        if args.rack is not None:
#            kwrags['rack'] = args.rack
#        if args.slot is not None:
#            kwargs['slots'] = args.slot
#        if args.cpu_count is not None:
#            kwargs['cpu_count'] = args.cpu_count
#        if args.cpu_mhz is not None:
#            kwargs['cpu_mhz'] = args.cpu_mhz
#        if args.memory is not None:
#            kwargs['mem_size'] = args.memory
#        host = client.hosts.create(**kwargs)
#        utils.print_dict(host)
#    except Exception as e:
#        utils.show_exception_and_exit(e)


@utils.arg('id', metavar='<HOST_ID>', help='ID of host to show')
@utils.arg('--with-meta', action='store_true', help='With meta data')
def do_host_show(client, args):
    """ Show details of a host """
    kwargs = {}
    if args.with_meta:
        kwargs['with_meta'] = True
    host = client.hosts.get(args.id, **kwargs)
    #print host
    #cluster = client.clusters.get(host.cluster_id)
    #host.cluster = cluster.name
    #host.zone_id = cluster.zone_id
    #zone = client.zones.get(cluster.zone_id)
    #host.zone = zone.name
    utils.print_dict(host)


@utils.arg('id', metavar='<HOST_ID>', help='ID of host to show')
def do_host_stats(client, args):
    """ Show statistics of a host """
    val = client.hosts.get_specific(args.id, 'stats')
    utils.print_dict(val)


@utils.arg('id', metavar='<HOST_ID>', help='ID of host to update')
@utils.arg('--name', metavar='<HOST_NAME>', help='Name of host')
@utils.arg('--ip', metavar='<ACCESS_IP>', help='Access IP of host')
@utils.arg('--manager-uri', metavar='<ACCESS_IP>', help='Access URI of this host')
@utils.arg('--desc', metavar='<HOST_DESC>', help='Description of host')
@utils.arg('--rack', metavar='<HOST_RACK>', help='Rack NO of host')
@utils.arg('--slot', metavar='<HOST_SLOT>', help='Slot NO of host')
@utils.arg('--cpu-count', metavar='<HOST_CPU_COUNT>', help='Number of CPU cores')
@utils.arg('--cpu-mhz', metavar='<HOST_CPU_HZ>', help='Frequency of CPU')
@utils.arg('--disk', metavar='<HOST_DISK_SIZE>', help='Size of disk in GB')
@utils.arg('--memory', metavar='<HOST_MEMORY>', help='Memory in MB')
@utils.arg('--cpu-commit-bound', metavar='<CPU_COMMIT_BOUND>', type=float, help='CPU overcommit upper bound at this host')
@utils.arg('--memory-commit-bound', metavar='<MEM_COMMIT_BOUND>', type=float, help='Memory overcommit upper bound at this host')
def do_host_update(client, args):
    """ Update a host """
    kwargs = {}
    if args.name is not None:
        kwargs['name'] = args.name
    if args.ip is not None:
        kwargs['access_ip'] = args.ip
    if args.manager_uri is not None:
        kwargs['manager_uri'] = args.manager_uri
    if args.desc is not None:
        kwargs['description'] = args.desc
    if args.rack is not None:
        kwargs['rack'] = args.rack
    if args.slot is not None:
        kwargs['slots'] = args.slot
    if args.cpu_count is not None:
        kwargs['cpu_count'] = args.cpu_count
    if args.cpu_mhz is not None:
        kwargs['cpu_mhz'] = args.cpu_mhz
    if args.memory is not None:
        kwargs['mem_size'] = args.memory
    if args.cpu_commit_bound is not None and args.cpu_commit_bound > 0:
        kwargs['cpu_cmtbound'] = args.cpu_commit_bound
    if args.memory_commit_bound is not None and args.memory_commit_bound > 0:
        kwargs['mem_cmtbound'] = args.memory_commit_bound
    if len(kwargs) == 0:
        raise Exception('No updates', 'Not enough data')
    host = client.hosts.update(args.id, **kwargs)
    utils.print_dict(host)

@utils.arg('id', metavar='<HOST_ID>', help='ID of host to set metadata info')
@utils.arg('--data', metavar='<KEY:VALUE>', action='append', help='Key:Value')
def do_host_set_metadata(client, args):
    """ Patch: set vip_reserved=True in 1.0.1
        to prevent small guests being scheduled to this host """
    kwargs = {}
    if args.data:
        for d in args.data:
            pos = d.find(':')
            if pos > 0:
                kwargs[d[:pos]] = d[(pos+1):]
            else:
                kwargs[d] = None
    else:
        raise Exception('No data to update')
    host = client.hosts.set_metadata(args.id, **kwargs)
    utils.print_dict(host)

@utils.arg('id', metavar='<HOST_ID>', help='ID of host to enable')
def do_host_enable(client, args):
    """ Enable a host """
    host = client.hosts.perform_action(args.id, 'enable')
    utils.print_dict(host)


@utils.arg('id', metavar='<HOST_ID>', help='ID of host to disable')
def do_host_disable(client, args):
    """ Enable a host """
    host = client.hosts.perform_action(args.id, 'disable')
    utils.print_dict(host)


@utils.arg('id', metavar='<HOST_ID>', help='ID of host to delete')
def do_host_delete(client, args):
    """ Delete a host """
    host = client.hosts.delete(args.id)
    utils.print_dict(host)


@utils.arg('id', metavar='<HOST_ID>', help='ID of host to balance')
def do_host_cpu_balance(client, args):
    """ Balance Host cpu """
    host = client.hosts.perform_action(args.id, 'cpu-node-balance')
    utils.print_dict(host)


def do_host_dynamic_load_updater(client, args):
    hosts = client.hosts.list(limit=0, details=False)[0]
    hosts = [host['id'] for host in hosts]
    usage_params = {'interval_unit': 'week', 'wire_id': '', 'interval': 1,
              'order': 'desc', 'storage_id': '', 'stat_field': '', 'page': 0}
    for host in hosts:
        typestr = 'cpu'
        usage = client.usages.get_host_usage(host, typestr, **usage_params)
        cpu_percent = usage[0]['percent'] if len(usage) > 0 else None
        typestr = 'io_stat'
        usage = client.usages.get_host_usage(host, typestr, **usage_params)
        disk_io_util = (usage[0]['io_stat_util']) if len(usage) > 0 else None   # of 100 percentage
        meta_data = {}
        if cpu_percent:
            meta_data['dynamic_load_cpu_percent'] = cpu_percent
        if disk_io_util:
            meta_data['dynamic_load_io_util'] = disk_io_util
        client.hosts.set_metadata(host, **meta_data)
        utils.print_dict(client.hosts.get_metadata(host))


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_wire_list(client, args):
    """ List all network broadcast areas """
    page_info = utils.get_paging_info(args)
    wires = client.wires.list(**page_info)
    utils.print_list(wires, client.wires.columns)


@utils.arg('name', metavar='<WIRE_NAME>', help='Name of wire (broadcast area) to create')
@utils.arg('--bw', metavar='<WIRE_BANDWIDTH>', required=True, help='Bandwidth of the wire (broadcast area)')
@utils.arg('--desc', metavar='<WIRE_DESCRIPTION>', help='Description')
def do_wire_create(client, args):
    """ Create a wire (broadcast area) """
    kwargs = {}
    kwargs['name'] = args.name
    kwargs['bandwidth'] = args.bw
    if args.desc is not None:
        kwargs['description'] = args.desc
    sub = client.wires.create(**kwargs)
    utils.print_dict(sub)


@utils.arg('id', metavar='<WIRE_ID>', help='Id of wire (broadcast area) to show')
def do_wire_show(client, args):
    """ Get detail of a wire (broadcast area) """
    sub = client.wires.get(args.id)
    utils.print_dict(sub)


@utils.arg('id', metavar='<WIRE_ID>', help='Id of wire to delete')
def do_wire_delete(client, args):
    """ Delete a wire (broadcast area) """
    sub = client.wires.delete(args.id)
    utils.print_dict(sub)


@utils.arg('id', metavar='<WIRE_ID>', help='Id of wire (broadcast area) to delete')
@utils.arg('--name', metavar='<WIRE_NAME>', help='Name of wire (broadcast area) to create')
@utils.arg('--bw', metavar='<WIRE_BANDWIDTH>', help='Bandwidth of the wire (broadcast area)')
@utils.arg('--desc', metavar='<WIRE_DESCRIPTION>', help='Description')
def do_wire_update(client, args):
    """ Update a wire (broadcast area) """
    kwargs = {}
    if args.name is not None:
        kwargs['name'] = args.name
    if args.bw is not None:
        kwargs['bandwidth'] = args.bw
    if args.desc is not None:
        kwargs['description'] = args.desc
    if len(kwargs) == 0:
        raise Exception("Not enough parameters", "NOt enough parameters")
    sub = client.wires.update(args.id, **kwargs)
    utils.print_dict(sub)


@utils.arg('id', metavar='<HOST_ID>', help='Id of host')
@utils.arg('--wire', metavar='<WIRE>', required=True, help='ID of wire')
@utils.arg('--bridge', metavar='<BRIDGE>', required=True, help='Name of bridge')
@utils.arg('--interface', metavar='<INTERFACE>', required=True, help='Interface associate with bridge')
def do_host_wire_attach(client, args):
    """ Attach a host to a wire (broadcast area) """
    kwargs = {}
    kwargs['bridge'] = args.bridge
    kwargs['interface'] = args.interface
    hs = client.hostwires.attach(args.id, args.wire, **kwargs)
    utils.print_dict(hs)


@utils.arg('id', metavar='<HOST_ID>', help='Id of host')
@utils.arg('--wire', metavar='<WIRE>', required=True, help='ID of wire')
def do_host_wire_detach(client, args):
    """ Detach a host from a wire """
    hs = client.hostwires.detach(args.id, args.wire)
    utils.print_dict(hs)


@utils.arg('id', metavar='<HOST_ID>', help='Id of host')
@utils.arg('--wire', metavar='<WIRE>', required=True, help='ID of wire')
def do_host_wire_show(client, args):
    """ Show how a host attach to a wire """
    hs = client.hostwires.get(args.id, args.wire)
    utils.print_dict(hs)


@utils.arg('--host', metavar='<HOST_ID>', help='ID of host')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_host_wire_list(client, args):
    """ List all substrates that a host joins """
    page_info = utils.get_paging_info(args)
    if args.host is None:
        hslist = client.hostwires.list(**page_info)
    else:
        hslist = client.hostwires.list_descendent(args.host, **page_info)
    utils.print_list(hslist, client.hostwires.columns)


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_storage_list(client, args):
    """ List all storages """
    page_info = utils.get_paging_info(args)
    storages = client.storages.list(**page_info)
    utils.print_list(storages, client.storages.columns)


@utils.arg('name', metavar='<STORAGE_NAME>', help='Name of storage')
@utils.arg('--capacity', metavar='<STORAGE_CAPACITY>', required=True, help='Capacity of storage in GB')
@utils.arg('--storage-type', metavar='<STORAGE_TYPE>', required=True, choices=['local', 'mebs'], help='Type of storage')
@utils.arg('--medium-type', metavar='<MEDIUM_TYPE>', choices=['ssd', 'rotational'], default='rotational', help='Type of storage medium')
@utils.arg('--commit-bound', metavar='<COMMIT_BOUND>', type=float, help='Upper bound of storage overcommit rate')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
@utils.arg('--mebs-manager-ip', metavar='<IP>', help='MEBS manager IP')
@utils.arg('--mebs-manager-port', metavar='<PORT>', type=int, help='MEBS manager port')
@utils.arg('--mebs-redis-ip', metavar='<IP>', help='MEBS redis IP')
@utils.arg('--mebs-redis-port', metavar='<PORT>', type=int, help='MEBS redis port')
@utils.arg('--mebs-sql-connection', metavar='<CONNECTION>', help='MEBS mysql connection')
def do_storage_create(client, args):
    """ Create a storage """
    kwargs = {}
    kwargs['name'] = args.name
    kwargs['capacity'] = int(args.capacity) * 1024 # convert to MB
    if args.storage_type is not None:
        kwargs['storage_type'] = args.storage_type
    if args.medium_type is not None:
        kwargs['medium_type'] = args.medium_type
    if args.commit_bound and args.commit_bound > 0.0:
        kwargs['cmtbound'] = args.commit_bound
    if args.desc is not None:
        kwargs['description'] = args.desc
    for k in ['mebs_manager_ip', 'mebs_manager_port',
              'mebs_redis_ip', 'mebs_redis_port',
              'mebs_sql_connection']:
        if getattr(args, k, None) is not None:
            kwargs[k] = getattr(args, k)
    storage = client.storages.create(**kwargs)
    utils.print_dict(storage)


@utils.arg('id', metavar='<STORAGE_ID>', help='ID of storage')
@utils.arg('--name', metavar='<STORAGE_NAME>', help='Name of storage')
@utils.arg('--capacity', metavar='<STORAGE_CAPACITY>', help='Capacity of storage')
@utils.arg('--storage-type', metavar='<STORAGE_TYPE>', choices=['local', 'mebs'], help='Type of storage')
@utils.arg('--medium-type', metavar='<MEDIUM_TYPE>', choices=['ssd', 'rotational'], help='Type of storage medium')
@utils.arg('--commit-bound', metavar='<COMMIT_BOUND>', type=float, help='Upper bound of storage overcommit rate')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
@utils.arg('--mebs-manager-ip', metavar='<IP>', help='MEBS manager IP')
@utils.arg('--mebs-manager-port', metavar='<PORT>', type=int, help='MEBS manager port')
@utils.arg('--mebs-redis-ip', metavar='<IP>', help='MEBS redis IP')
@utils.arg('--mebs-redis-port', metavar='<PORT>', type=int, help='MEBS redis port')
@utils.arg('--mebs-sql-connection', metavar='<CONNECTION>', help='MEBS mysql connection')
def do_storage_update(client, args):
    """ Update a storage """
    kwargs = {}
    if args.name is not None:
        kwargs['name'] = args.name
    if args.capacity is not None:
        kwargs['capacity'] = int(args.capacity) * 1024
    if args.storage_type is not None:
        kwargs['storage_type'] = args.storage_type
    if args.medium_type is not None:
        kwargs['medium_type'] = args.medium_type
    if args.commit_bound and args.commit_bound > 0.0:
        kwargs['cmtbound'] = args.commit_bound
    if args.desc is not None:
        kwargs['description'] = args.desc
    for k in ['mebs_manager_ip', 'mebs_manager_port',
                'mebs_redis_ip', 'mebs_redis_port',
                'mebs_sql_connection']:
        if getattr(args, k, None) is not None:
            kwargs[k] = getattr(args, k)
    if len(kwargs) == 0:
        raise Exception("No data", "No data")
    storage = client.storages.update(args.id, **kwargs)
    utils.print_dict(storage)


@utils.arg('id', metavar='<STORAGE_ID>', help='ID of storage')
def do_storage_show(client, args):
    """ Show details of a storage """
    storage = client.storages.get(args.id)
    utils.print_dict(storage)


@utils.arg('id', metavar='<STORAGE_ID>', help='ID of storage')
def do_storage_delete(client, args):
    """ Delete a storage """
    storage = client.storages.delete(args.id)
    utils.print_dict(storage)


@utils.arg('--host', metavar='<HOST_ID>', help='ID of host')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_host_storage_list(client, args):
    """ List storages of a host """
    page_info = utils.get_paging_info(args)
    if args.host is not None:
        hoststorages = client.hoststorages.list_descendent(args.host,
                                                                **page_info)
    else:
        hoststorages = client.hoststorages.list(**page_info)
    utils.print_list(hoststorages, client.hoststorages.columns)


@utils.arg('id', metavar='<HOST_ID>', help='ID of host')
@utils.arg('--storage', metavar='<STORAGE_ID>', required=True, help='ID of storage')
@utils.arg('--mount-point', metavar='<STORAGE_MOUNT_POINT>', required=True, help='Mount path of storage on host')
def do_host_storage_attach(client, args):
    """ Atach a host to a storage """
    kwargs = {}
    kwargs['mount_point'] = args.mount_point
    hoststorage = client.hoststorages.attach(args.id, args.storage, **kwargs)
    utils.print_dict(hoststorage)


@utils.arg('id', metavar='<HOST_ID>', help='ID of host')
@utils.arg('--storage', metavar='<STORAGE_ID>', required=True, help='ID of storage')
def do_host_storage_detach(client, args):
    """ Detach a host from a storage """
    hoststorage = client.hoststorages.detach(args.id, args.storage)
    utils.print_dict(hoststorage)


@utils.arg('id', metavar='<HOST_ID>', help='ID of host')
@utils.arg('--storage', metavar='<STORAGE_ID>', required=True, help='ID of storage')
def do_host_storage_show(client, args):
    """ Show how a host attach to a storage """
    hoststorage = client.hoststorages.get(args.id, args.storage)
    utils.print_dict(hoststorage)


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_edge_list(client, args):
    """ List all edge routers """
    page_info = utils.get_paging_info(args)
    edges = client.edges.list(**page_info)
    utils.print_list(edges, client.edges.columns)


@utils.arg('id', metavar='<ZONE_ID>', help='ID of zone')
@utils.arg('--name', metavar='<NAME>', required=True, help='Name of edge router')
@utils.arg('--ip', metavar='<IP>', required=True, help='Admininistrative IP address of edge router')
@utils.arg('--port', metavar='<PORT>', help='Administrative port of edge router')
@utils.arg('--proto', metavar='<PROTOCOL>', required=True, choices=['ssh', 'telnet'], help='Admininistrative protocol (ssh or telnet)')
@utils.arg('--user', metavar='<AUTH_USER>', required=True, help='Admininistrative account')
@utils.arg('--key-file', metavar='<SSH_PRIVATE_KEY>', help='Authentication private key')
@utils.arg('--passwd', metavar='<PASSWORD>', help='Authentication password')
@utils.arg('--model', metavar='<MODEL>', choices=['ubuntu', 'debian'], help='Model of edge router')
@utils.arg('--egress', metavar='<EGRESS_IF_NAME>', required=True, help='Egress interface name of edge router')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
def do_zone_create_edge(client, args):
    """ Create an edge router """
    kwargs = {}
    kwargs['name'] = args.name
    kwargs['admin_ip'] = args.ip
    kwargs['admin_proto'] = args.proto
    kwargs['auth_user'] = args.user
    kwargs['egress_if'] = args.egress
    if args.model:
        if args.model == 'ubuntu' or args.model == 'debian':
            kwargs['driver'] = 'LinuxDebian'
        else:
            raise Exception('Unsupported model')
    if args.key_file is not None:
        auth_data = {}
        with open(args.key_file) as kf:
            auth_data['key'] = kf.read()
        if args.passwd is not None:
            auth_data['pass'] = args.passwd
        kwargs['auth_data'] = json.dumps(auth_data)
        kwargs['auth_scheme'] = 'key'
    elif args.passwd is not None:
        kwargs['auth_data'] = args.passwd
        kwargs['auth_scheme'] = 'password'
    else:
        raise Exception('Please specify --key-file or --passwd')
    if args.desc:
        kwargs['description'] = args.desc
    if args.port and int(args.port) > 0:
        kwargs['admin_port'] = int(args.port)
    edge = client.zones.create_descendent(args.id,
                    yunionclient.api.edges.EdgeManager, **kwargs)
    utils.print_dict(edge)


@utils.arg('id', metavar='<EDGE_ID>', help='ID of edge router')
def do_edge_show(client, args):
    """ Show details of an edge router """
    edge = client.edges.get(args.id)
    utils.print_dict(edge)


@utils.arg('id', metavar='<EDGE_ID>', help='ID of edge router')
@utils.arg('--name', metavar='<NAME>', help='Name of edge router')
@utils.arg('--ip', metavar='<IP>', help='Admininistrative IP address of edge router')
@utils.arg('--port', metavar='<PORT>', help='Administrative port of edge router')
@utils.arg('--proto', metavar='<PROTOCOL>', choices=['ssh', 'telnet'], help='Admininistrative protocol (ssh or telnet)')
@utils.arg('--user', metavar='<AUTH_USER>', help='Admininistrative account')
@utils.arg('--key-file', metavar='<SSH_PUBLIC_KEY>', help='Authentication public key')
@utils.arg('--passwd', metavar='<PASSWORD>', help='Authentication password')
@utils.arg('--model', metavar='<MODEL>', choices=['ubuntu'], help='Model of edge router')
@utils.arg('--egress', metavar='<EGRESS_IF_NAME>', help='Egress interface name of edge router')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
def do_edge_update(client, args):
    """ Update an edge router """
    kwargs = {}
    if args.name:
        kwargs['name'] = args.name
    if args.ip:
        kwargs['admin_ip'] = args.ip
    if args.port and int(args.port) > 0:
        kwargs['admin_port'] = int(args.port)
    if args.proto:
        kwargs['admin_proto'] = args.proto
    if args.user:
        kwargs['auth_user'] = args.user
    if args.egress:
        kwargs['egress_if'] = args.egress
    if args.model:
        if args.model == 'ubuntu' or args.model == 'debian':
            kwargs['driver'] = 'LinuxDebian'
        else:
            raise Exception('Unsupported model')
    if args.key_file is not None:
        auth_data = {}
        with open(args.key_file) as kf:
            auth_data['key'] = kf.read()
        if args.passwd is not None:
            auth_data['pass'] = args.passwd
        kwargs['auth_data'] = json.dumps(auth_data)
        kwargs['auth_scheme'] = 'key'
    elif args.passwd is not None:
        kwargs['auth_data'] = args.passwd
        kwargs['auth_scheme'] = 'password'
    if args.desc:
        kwargs['description'] = args.desc
    if len(kwargs) == 0:
        raise Exception('No data to update')
    edge = client.edges.update(args.id, **kwargs)
    utils.print_dict(edge)


@utils.arg('id', metavar='<EDGE_ID>', help='ID of edge router')
def do_edge_delete(client, args):
    """ Delete an edge router """
    edge = client.edges.delete(args.id)
    utils.print_dict(edge)


@utils.arg('id', metavar='<EDGE_ID>', help='ID of edge router to sync config')
def do_edge_sync(client, args):
    """ Sync configuration with an edge router """
    edge = client.edges.perform_action(args.id, 'sync')
    utils.print_dict(edge)


@utils.arg('id', metavar='<EDGE_ID>', help='ID of edge router')
@utils.arg('--wire', metavar='<WIRE_ID>', required=True, help='ID of wire to attach')
def do_edge_wire_attach(client, args):
    """ Attach an edge router to a wire """
    ew = client.edgewires.attach(args.id, args.wire)
    utils.print_dict(ew)


@utils.arg('id', metavar='<EDGE_ID>', help='ID of edge router')
@utils.arg('--wire', required=True, metavar='<WIRE_ID>', help='ID of wire to attach')
def do_edge_wire_detach(client, args):
    """ Detach an edge router to a wire """
    ew = client.edgewires.detach(args.id, args.wire)
    utils.print_dict(ew)


@utils.arg('--edge', metavar='<EDGE_ID>', help='ID of edge router')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_edge_wire_list(client, args):
    """ List all wires attached to an edge router """
    page_info = utils.get_paging_info(args)
    if args.edge:
        ews = client.edgewires.list_descendent(args.edge, **page_info)
    else:
        ews = client.edgewires.list(**page_info)
    utils.print_list(ews, client.edgewires.columns)


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_eip_list(client, args):
    """ List of elastic IPs """
    page_info = utils.get_paging_info(args)
    eips = client.elasticips.list(**page_info)
    utils.print_list(eips, client.elasticips.columns)


@utils.arg('id', metavar='<EDGE_ID>', help='ID of edge router')
@utils.arg('--name', metavar='<EIP>', required=True, help='Elastic IP address')
@utils.arg('--ifname', metavar='<IFNAME>', required=True, help='Interface')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
def do_edge_create_eip(client, args):
    """ Create an elstic IP on an edge router """
    kwargs = {}
    kwargs['name'] = args.name
    kwargs['ifname'] = args.ifname
    if args.desc:
        kwargs['description'] = args.desc
    eip = client.edges.create_descendent(args.id,
                    yunionclient.api.elasticips.ElasticipManager, **kwargs)
    utils.print_dict(eip)


@utils.arg('id', metavar='<EIP_ID>', help='ID of EIP')
@utils.arg('--name', metavar='<EIP>', help='Elastic IP address')
@utils.arg('--ifname', metavar='<IFNAME>', help='Interface')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
def do_eip_update(client, args):
    """ Update an elstic IP on an edge router """
    kwargs = {}
    if args.name:
        kwargs['name'] = args.name
    if args.ifname:
        kwargs['ifname'] = args.ifname
    if args.desc:
        kwargs['description'] = args.desc
    if len(kwargs) == 0:
        raise Exception('No data to update')
    eip = client.elasticips.update(args.id, **kwargs)
    utils.print_dict(eip)


@utils.arg('id', metavar='<EIP_ID>', help='ID of EIP')
def do_eip_show(client, args):
    """ Show details of an elstic IP on an edge router """
    eip = client.elasticips.get(args.id)
    utils.print_dict(eip)


@utils.arg('id', metavar='<EIP_ID>', help='ID of EIP')
def do_eip_delete(client, args):
    """ Delete an elstic IP on an edge router """
    eip = client.elasticips.delete(args.id)
    utils.print_dict(eip)


@utils.arg('id', metavar='<SERVER>', help='ID of virtual server')
@utils.arg('--proto', metavar='<PROTOCOL>', choices=['tcp', 'udp'], help='Layer 4 protocol')
@utils.arg('--port', metavar='<PORT>', help='Port number')
@utils.arg('--net', metavar='<NETWORK>', help='Specify the virtual NIC that server attach to')
@utils.arg('--eip', metavar='<EGRESS_IP>', help='Specify egress IP address, otherwise, it is assigned by system')
@utils.arg('--eport', metavar='<EGRESS_PORT>', help='Specify egress port, otherwise, it is the same as port')
def do_server_eip_add(client, args):
    """ Map server port to public IP/port """
    kwargs = {}
    if args.proto:
        kwargs['proto'] = args.proto
    if args.port:
        kwargs['port'] = int(args.port)
    if args.net:
        kwargs['net_id'] = args.net
    if args.eip:
        kwargs['eip'] = args.eip
    if args.eport:
        kwargs['eport'] = int(args.eport)
    guest = client.guests.perform_action(args.id, 'addeip', **kwargs)
    utils.print_dict(guest)


@utils.arg('--server', metavar='<SERVER>', help='ID of virtual server')
@utils.arg('--eip', metavar='<EIP>', help='Elastic IP')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_server_eip_list(client, args):
    """ List all eip of a virtual server """
    kwargs = utils.get_paging_info(args)
    if args.server:
        kwargs['guest'] = args.server
    if args.eip:
        kwargs['eip'] = args.eip
    portmaps = client.portmaps.list(**kwargs)
    columns = ['Guest_id', 'Guest', 'IP', 'Port', 'Protocol', 'EIP', 'EPort']
    utils.print_list(portmaps, columns)


@utils.arg('id', metavar='<SERVER>', help='ID of virtual server')
@utils.arg('--eip', metavar='<EGRESS_IP>', help='Specify egress IP address to remove')
@utils.arg('--proto', metavar='<PROTOCOL>', choices=['tcp', 'udp'], help='Layer 4 protocol')
@utils.arg('--port', metavar='<PORT>', help='Port number')
@utils.arg('--eport', metavar='<EGRESS_PORT>', help='Specify egress port, otherwise, it is the same as port')
def do_server_eip_remove(client, args):
    """ Delete an eip from a virtual server """
    kwargs = {}
    if args.proto:
        kwargs['proto']  = args.proto
    if args.port:
        kwargs['port']   = int(args.port)
    if args.eip:
        kwargs['eip']    = args.eip
    if args.eport:
        kwargs['eport']  = int(args.eport)
    guest = client.guests.perform_action(args.id, 'deleip', **kwargs)
    utils.print_dict(guest)


########################### VNC #####################################

@utils.arg('id', metavar='<SERVER_ID>', help='ID of server to connect')
def do_vnc_connect(client, args):
    """ get a link to connect to virtual server """
    info = client.vncproxy.connect(args.id)
    utils.print_dict(info)


@utils.arg('id', metavar='<BAREMETAL_ID>', help='ID of baremetal to connect')
def do_vnc_connect_baremetal(client, args):
    """ get a link to connect to baremetal server """
    info = client.vncproxy.connect(args.id, 'baremetals')
    utils.print_dict(info)


def do_ssh_connections(client, args):
    """ Show ssh connections """
    info = client.sshrelay.get_connections()
    utils.print_list(info, ['Created', 'Address', 'Status', 'User', 'Tenant', 'Peer'])


############################## Usages ##############################


def _show_usage_results(args, result):
    if result:
        if args.type is None:
            utils.print_dict(result['usage'])
        elif args.stat_func:
            utils.print_dict(result)
        else:
            fields = sorted(list(result[0].keys()), key=lambda x: _g(x))
            utils.print_list(result, fields)
    else:
        print("Empty set.")


def _g(x):
    "to sort pretty table header"

    pre_defined_header_order = ['created_at', 'id', 'guest_id', 'host_id', 'storage_id', 'wire_id']
    if x in pre_defined_header_order:
        return pre_defined_header_order.index(x)
    else:
        return x

@utils.arg('id', metavar='<SERVER_ID>', help='ID of server to query')
@utils.arg('--type', metavar='<METRICS_NAME>', required=False,
           help='Name of metrics to query, choose from `cpu`, `io`, `net_external`, `net_internal`, `net`(alias for net_external).',
           choices=['cpu', 'io', 'net', 'net_external', 'net_internal'])
@utils.arg('--count', required=False, \
           help='How many items to be returned on each page; Default is 20.', default=20)
@utils.arg('--page', required=False, \
           help='Which page to show. Default is 0.', default=0)
@utils.arg('--interval', required=False,
           help='Specify time interval between each item.', default=1)
@utils.arg('--interval_unit', required=False,
           help='Specify time unit for INTERVAL argument.',
           default='minute', choices=['minute', 'hour', 'day', 'week', 'month', 'year'])
@utils.arg('--order', required=False,
           help='Sort the items in ascending/descending order.',
           default='desc', choices=['desc', 'asc'])
@utils.arg('--since', required=False, \
           help='Since when the monitor log to show. UTC+0000 Time used. Default {today} 00:00:00.', \
           default='')
@utils.arg('--until', required=False, \
           help='Until when the monitor log to show. UTC+0000 Time used. Default {today} 23:59:59.', \
           default='')
@utils.arg('--stat_func', required=False, \
           help='''get the Max/Min/Sum/Avg value between a range of time.
           Please do specify a type, like `percentage` for cpu,
           `bytes_recv_per_min` for net, etc. Must be  one of max, min, sum, avg''',
           default='', choices=['max', 'min', 'sum', 'avg', 'count'])
@utils.arg('--stat_field', required=False, \
           help='''Specify which field to query, related to the class. Example, `percentage` of cpu.''',
           default='')
def do_server_usage(client, args):
    """ Get the monitoring metrics of a virtual server """
    result = client.usages.get_guest_usage(args.id, args.type,
                                               count=args.count,
                                               page=args.page,
                                               interval=args.interval,
                                               interval_unit=args.interval_unit,
                                               order=args.order,
                                               since=args.since,
                                               until=args.until,
                                               stat_func=args.stat_func,
                                               stat_field=args.stat_field,
                                               )
    _show_usage_results(args, result)

@utils.arg('id', metavar='<HOST_ID>', help='ID of host to query')
@utils.arg('--type', metavar='<METRICS_NAME>', required=False,
           help='Name of metrics to query, choose from `cpu`, `memory`,'
           '`storage`, `cpu_no` for used cpu number, `io_stat`, `net_bridge`, `net_phys`, `net`(alias for net_bridge).',
           choices=['cpu', 'memory', 'storage', 'cpu_no', 'io_stat', 'net', 'net_bridge', 'net_phys'])
@utils.arg('--count', required=False,
           help='How many items to be returned on each page; Default is 20.', default=20)
@utils.arg('--page', required=False,
           help='Which page to show. Default is 0.', default=0)
@utils.arg('--interval', required=False,
           help='Specify time interval between each item.', default=1)
@utils.arg('--interval_unit', required=False,
           help='Specify time unit for INTERVAL argument.',
           default='minute', choices=['minute', 'hour', 'day', 'week', 'month', 'year'])
@utils.arg('--order', required=False,
           help='Sort the items in ascending/descending order.',
           default='desc', choices=['desc', 'asc'])
@utils.arg('--since', required=False,
           help='Since when the monitor log to show. UTC+0000 Time used. Default {today} 00:00:00.',
           default='')
@utils.arg('--until', required=False, \
           help='Until when the monitor log to show. UTC+0000 Time used. Default {today} 23:59:59.', \
           default='')
@utils.arg('--storage_id', required=False, help='Only applicable for storage usage query.',
           default='')
@utils.arg('--wire_id', required=False, help='Only applicable for net usage query.',
           default='')
@utils.arg('--stat_func', required=False,
           help='''get the Max/Min/Sum/Avg value between a range of time.
           Please do specify a type, like `percentage` for cpu,
           `bytes_recv_per_min` for net, etc. Must be  one of max, min, sum, avg''',
           default='', choices=['max', 'min', 'sum', 'avg', 'count'])
@utils.arg('--stat_field', required=False,
           help='''Specify which field to query, related to the class. Example, `percentage` of cpu.''',
           default='')
def do_host_usage(client, args):
    """ Get the monitoring metrics of a host """
    result = client.usages.get_host_usage(args.id, args.type,
                                              count=args.count,
                                              page=args.page,
                                              interval=args.interval,
                                              interval_unit=args.interval_unit,
                                              order=args.order,
                                              since=args.since,
                                              until=args.until,
                                              storage_id=args.storage_id,
                                              wire_id=args.wire_id,
                                              stat_func=args.stat_func,
                                              stat_field=args.stat_field,
                                              )
    _show_usage_results(args, result)


@utils.arg('id', metavar='<CLUSTER_ID>', help='ID of cluster to query')
@utils.arg('--type', metavar='<METRICS_NAME>', required=False,
           help='Name of metrics to query')
@utils.arg('--count', required=False, help='How many items to be returned on each page; Default is 20.', default=20)
@utils.arg('--page', required=False, help='Which page to show. Default is 0.',
           default=0)
@utils.arg('--since', required=False, help='Since when the monitor log to show. UTC+0000 Time used. Default None.',
           default='')
def do_cluster_usage(client, args):
    """ Get the monitoring metrics of a cluster """
    result = client.usages.get_cluster_usage(args.id, args.type,
                                                 count=args.count,
                                                 page=args.page,
                                                 since=args.since,
                                                 )
    _show_usage_results(args, result)


@utils.arg('id', metavar='<ZONE_ID>', help='ID of zone to query')
@utils.arg('--type', metavar='<METRICS_NAME>', required=False, help='Name of metrics to query')
@utils.arg('--count', required=False, help='How many items to be returned on each page; Default is 20.', default=20)
@utils.arg('--page', required=False, help='Which page to show. Default is 0.',
           default=0)
@utils.arg('--since', required=False, help='Since when the monitor log to show. UTC+0000 Time used. Default None.', default='')
@utils.arg('--aggregate', metavar='<AGGREGATE>', action='append', help='Aggregate ID or name')
def do_zone_usage(client, args):
    """ Get the monitoring metrics of a zone """
    kwargs = {}
    if args.count is not None:
        kwargs['count'] = args.count
    if args.page is not None:
        kwargs['page'] = args.page
    if args.since is not None:
        kwargs['since'] = args.since
    if args.aggregate:
        index = 0
        for aggregate in args.aggregate:
            kwargs['aggregate.%d' % index] = aggregate
            index += 1
    result = client.usages.get_zone_usage(args.id, args.type, **kwargs)
    _show_usage_results(args, result)


def do_usage(client, args):
    """ Get general monitoring metrics """
    result = client.usages.get_usage_general()
    utils.print_dict(result['usage'])


def do_region_list(client, args):
    """ List all regions """
    regions = client.get_regions()
    columns = ['Region', 'publicURL', 'internalURL']
    utils.print_list(regions, columns)


def do_current_user(client, args):
    """ Show current user info """
    tenant = client.get_default_tenant()
    if tenant is None:
        raise Exception('No active tenant')
    import copy
    info = copy.deepcopy(tenant.get_user_info())
    info.update({
                'tenant': tenant.get_name(),
                'tenant_id': tenant.get_id(),
                'token': tenant.get_token(),
                })
    utils.print_dict(info)


def do_current_user_tenant_list(client, args):
    """ List user's tenant """
    tenants = client.get_tenants()
    columns = ['ID', 'Name']
    utils.print_list(tenants, columns)


################ QUOTA ######################


@utils.arg('--tenant', metavar='<TENANT>', help='Tenant name or ID')
@utils.arg('--user', metavar='<USER>', help='User name or ID')
def do_quota(client, args):
    """ Show user quota """
    quota = client.quotas.get(args.tenant, args.user)
    utils.print_dict(quota)


@utils.arg('--tenant', metavar='<TENANT>', help='Tenant name or ID')
@utils.arg('--cpu', metavar='<#CPU>', help='Number of CPU cores')
@utils.arg('--memory', metavar='<MB>', help='Size of memory in MB')
@utils.arg('--storage', metavar='<MB>', help='Size of storage in MB')
@utils.arg('--port', metavar='<#PORT>', help='Number of network ports')
@utils.arg('--eip', metavar='<#EIP>', help='Elastic IPs')
@utils.arg('--eport', metavar='<#EPORT>', help='External network port')
@utils.arg('--bw', metavar='<#BANDWIDTH>', help='Bandwidth')
@utils.arg('--ebw', metavar='<#EBANDWIDTH>', help='External bandwidth')
@utils.arg('--image', metavar='<#IMAGE>', help='Number of images')
@utils.arg('--redis', metavar='<#REDIS>', help='Number of redis')
@utils.arg('--rds', metavar='<#RDS>', help='Number of rds')
@utils.arg('--secgroup', metavar='<#SECGROUP>', type=int, help='Number of security groups')
@utils.arg('--snapshot', metavar='<#SNAPSHOT>', type=int, help='Number of snapshots')
def do_quota_set(client, args):
    """ Set user quota """
    kwargs = {}
    if args.cpu:
        kwargs['cpu'] = args.cpu
    if args.memory:
        kwargs['memory'] = args.memory
    if args.storage:
        kwargs['storage'] = args.storage
    if args.port:
        kwargs['port'] = args.port
    if args.eip:
        kwargs['eip'] = args.eip
    if args.eport:
        kwargs['eport'] = args.eport
    if args.bw:
        kwargs['bw'] = args.bw
    if args.ebw:
        kwargs['ebw'] = args.ebw
    if args.image:
        kwargs['image'] = args.image
    if args.redis:
        kwargs['redis'] = int(args.redis)
    if args.rds:
        kwargs['rds'] = int(args.rds)
    if args.secgroup:
        kwargs['secgroup'] = args.secgroup
    if args.snapshot:
        kwargs['snapshot'] = args.snapshot

    if len(kwargs) == 0:
        raise Exception('No data to update')
    quota = client.quotas.set(args.tenant, **kwargs)
    utils.print_dict(quota)


@utils.arg('--tenant', metavar='<TENANT>', required=True, help='Tenant name or ID')
@utils.arg('--cpu', metavar='<#CPU>', type=int, help='Number of CPU cores')
@utils.arg('--memory', metavar='<MB>', type=int, help='Size of memory in MB')
@utils.arg('--storage', metavar='<MB>', type=int, help='Size of storage in MB')
@utils.arg('--port', metavar='<#PORT>', type=int, help='Number of network ports')
@utils.arg('--eip', metavar='<#EIP>', type=int, help='Elastic IPs')
@utils.arg('--eport', metavar='<#EPORT>', type=int, help='External network port')
@utils.arg('--bw', metavar='<#BANDWIDTH>', type=int, help='Bandwidth')
@utils.arg('--ebw', metavar='<#EBANDWIDTH>', type=int, help='External bandwidth')
@utils.arg('--image', metavar='<#IMAGE>', type=int, help='Number of images')
@utils.arg('--redis', metavar='<#REDIS>', type=int, help='Number of redis')
@utils.arg('--secgroup', metavar='<#SECGROUP>', type=int, help='Number of security groups')
@utils.arg('--snapshot', metavar='<#SNAPSHOT>', type=int, help='Number of snapshots')
@utils.arg('--keypair', metavar='<#KEYPAIR>', type=int, help='Number of keypairs')
@utils.arg('--group', metavar='<#GROUP>', type=int, help='Number of groups')
@utils.arg('--vpc', metavar='<#VPC>', type=int, help='Number of vpc')
def do_quota_check(client, args):
    """ Check user quota """
    kwargs = {}
    if args.cpu:
        kwargs['cpu_count'] = args.cpu
    if args.memory:
        kwargs['memory_size'] = args.memory
    if args.storage:
        kwargs['disk_size'] = args.storage
    if args.port:
        kwargs['nic_count'] = args.port
    if args.eip:
        kwargs['eip_count'] = args.eip
    if args.eport:
        kwargs['enic_count'] = args.eport
    if args.bw:
        kwargs['bw'] = args.bw
    if args.ebw:
        kwargs['ebw'] = args.ebw
    if args.image:
        kwargs['image'] = args.image
    if args.redis:
        kwargs['redis'] = args.redis
    if args.secgroup:
        kwargs['secgroup'] = args.secgroup
    if args.snapshot:
        kwargs['snapshot'] = args.snapshot
    if args.keypair:
        kwargs['keypair'] = args.keypair
    if args.group:
        kwargs['group'] = args.group
    if args.vpc:
        kwargs['vpc'] = args.vpc

    if len(kwargs) == 0:
        raise Exception('No data to check')
    ret = client.quotas.check(args.tenant, **kwargs)
    if len(ret) > 0:
        print(ret)
    else:
        print('Successful')


################ IP ######################
@utils.arg('ip', metavar='<IP>', nargs='+', help='IP address')
def do_ip_search(client, args):
    # Use IP to look up user and server info
    for each_ip in args.ip:
        result = {}
        filter_clause = "ip_addr.equals('%s')" % each_ip
        kwargs = {'filter.0': filter_clause}
        guestnetworks = client.guestnetworks.list(**kwargs)
        if guestnetworks[0]:
            for each in guestnetworks[0]:
                guest = client.guests.get(each['guest_id'])
                result.update(type="guest",
                              server=guest['name'],
                              server_id=guest['id'],
                              user_id=guest['user_id'])
                user_info = client.users.get(guest['user_id'])
                result.update(user=user_info['name'],
                              mobile=user_info['mobile'],
                              email=user_info['email'],
                              tenant=user_info['tenant_name'],
                              tenant_id=user_info['tenantId'])
                utils.print_dict(result)
        else:
            baremetalnetworks = client.baremetalnetworks.list(**kwargs)
            if baremetalnetworks[0]:
                for each in baremetalnetworks[0]:
                    guest = client.baremetals.get(each['baremetal_id'])
                    result.update(type="baremetal",
                                baremetal=guest['name'],
                                baremetal_id=guest['id'])
                    utils.print_dict(result)
            else:
                ips = client.reservedips.list(**kwargs)
                if ips[0]:
                    for each in ips[0]:
                        result.update(type="reserved_ip",
                                    network_id=each['network_id'],
                                    ip_addr=each['ip_addr'],
                                    network=each['network'])
                        utils.print_dict(result)
                else:
                    raise Exception("Cann't find the IP :'%s'" %each_ip)
