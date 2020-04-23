import yunionclient

from yunionclient.common import utils

import json


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--admin', action='store_true', help='Is admin call?')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant ID or Name')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
@utils.arg('--type', metavar='<TYPE>', choices=['guest', 'baremetal'], help='Server type of the networks. List all if not specify')
def do_network_list(client, args):
    """ List all virtual networks """
    page_info = utils.get_paging_info(args)
    if args.type:
        page_info['server_type'] = args.type
    nets = client.networks.list(**page_info)
    utils.print_list(nets, client.networks.columns)


@utils.arg('id', metavar='<WIRE_ID>', help='Substrate id')
@utils.arg('--name', metavar='<NETWORK_NAME>', required=True, help='Name of network to create')
@utils.arg('--start-ip', metavar='<NETWORK_START_IP>', required=True, help='Start ip of network')
@utils.arg('--end-ip', metavar='<NETWORK_END_IP>', required=True, help='End ip of network')
@utils.arg('--netmask', metavar='<NETWORK_MASK>', required=True, help='Network mask length')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
@utils.arg('--gateway', metavar='<GATEWAY>', help='Default gateway')
@utils.arg('--dns', metavar='<DNS>', help='DNS server')
@utils.arg('--domain', metavar='<DOMAIN>', help='Default domain')
@utils.arg('--dhcp', metavar='<DHCP>', help='DHCP server')
#@utils.arg('--vlan', metavar='<VLAN_ID>', help='vlan ID')
@utils.arg('--type', metavar='<TYPE>', choices=['guest', 'baremetal'], help='Server type of the networks')
def do_wire_create_network(client, args):
    """ Create a virtual network over a wire """
    kwargs = {}
    kwargs['name'] = args.name
    kwargs['guest_ip_start'] = args.start_ip
    kwargs['guest_ip_end'] = args.end_ip
    kwargs['guest_ip_mask'] = args.netmask
    #kwargs['wire_id']   = args.id
    if args.desc is not None:
        kwargs['description'] = args.desc
    if args.gateway is not None:
        kwargs['guest_gateway'] = args.gateway
    if args.dns is not None:
        kwargs['guest_dns'] = args.dns
    if args.dhcp is not None:
        kwargs['guest_dhcp'] = args.dhcp
    if args.domain is not None:
        kwargs['guest_domain'] = args.domain
    if args.type:
        kwargs['server_type'] = args.type
    #if args.vlan is not None:
    #    kwargs['vlan_id'] = args.vlan
    net = client.wires.create_descendent(args.id,
                        yunionclient.api.networks.NetworkManager, **kwargs)
    utils.print_dict(net)


@utils.arg('id', metavar='<NETWORK_ID>', help='ID of network to show')
def do_network_show(client, args):
    """ Show details of a virtual network """
    net = client.networks.get(args.id)
    utils.print_dict(net)


@utils.arg('id', metavar='<NETWORK_ID>', help='ID of virtual network to get metadata info')
@utils.arg('--field', metavar='<METADATA_FIELD>', help='Field name of metadata')
def do_network_metadata(client, args):
    """ Show metadata info of a virtual network """
    kwargs = {}
    if args.field is not None:
        kwargs['field'] = args.field
    meta = client.networks.get_metadata(args.id, **kwargs)
    if isinstance(meta, dict):
        utils.print_dict(meta)
    else:
        print(meta)


@utils.arg('id', metavar='<NETWORK_ID>', help='ID of virtual network to get metadata info')
@utils.arg('--key', metavar='<KEYNAME>', help='Key name of secret')
@utils.arg('--secret', metavar='<SECRET>', help='Key secret')
@utils.arg('--server', metavar='<SECRET>', help='Alternate DNS update server')
def do_network_set_dns_update_key(client, args):
    """ Set DNS update key info for a virtual network """
    kwargs = {}
    kwargs['dns_update_key_name'] = args.key
    kwargs['dns_update_key_secret'] = args.secret
    kwargs['dns_update_server'] = args.server
    net = client.networks.set_metadata(args.id, **kwargs)
    utils.print_dict(net)


@utils.arg('id', metavar='<NETWORK_ID>', help='ID of virtual network to get metadata info')
def do_network_remove_dns_update_key(client, args):
    """ Set DNS update key info for a virtual network """
    kwargs = {}
    kwargs['dns_update_key_name'] = 'None'
    kwargs['dns_update_key_secret'] = 'None'
    kwargs['dns_update_server'] = 'None'
    net = client.networks.set_metadata(args.id, **kwargs)
    utils.print_dict(net)


@utils.arg('id', metavar='<NETWORK_ID>', help='ID of network to show')
@utils.arg('--name', metavar='<NETWORK_NAME>', help='Name of network to create')
@utils.arg('--start-ip', metavar='<NETWORK_START_IP>', help='Start ip of network')
@utils.arg('--end-ip', metavar='<NETWORK_END_IP>', help='End ip of network')
@utils.arg('--netmask', metavar='<NETWORK_MASK>', help='Network mask length')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
@utils.arg('--gateway', metavar='<GATEWAY>', help='Default gateway')
@utils.arg('--dns', metavar='<DNS>', help='DNS server')
@utils.arg('--domain', metavar='<DOMAIN>', help='Default domain')
@utils.arg('--dhcp', metavar='<DHCP>', help='DHCP server')
#@utils.arg('--vlan', metavar='<VLAN_ID>', help='vlan ID')
def do_network_update(client, args):
    """ Update a virtual network """
    kwargs = {}
    if args.name is not None:
        kwargs['name'] = args.name
    if args.start_ip is not None:
        kwargs['guest_ip_start'] = args.start_ip
    if args.end_ip is not None:
        kwargs['guest_ip_end'] = args.end_ip
    if args.netmask is not None:
        kwargs['guest_ip_mask'] = args.netmask
    if args.desc is not None:
        kwargs['description'] = args.desc
    if args.gateway is not None:
        kwargs['guest_gateway'] = args.gateway
    if args.dns is not None:
        kwargs['guest_dns'] = args.dns
    if args.dhcp is not None:
        kwargs['guest_dhcp'] = args.dhcp
    if args.domain is not None:
        kwargs['guest_domain'] = args.domain
    #if args.vlan is not None:
    #    kwargs['vlan_id'] = args.vlan
    if len(kwargs) == 0:
        raise Exception("Empty data", "empty data")
    net = client.networks.update(args.id, **kwargs)
    utils.print_dict(net)


@utils.arg('id', metavar='<NETWORK_ID>', help='ID of network to delete')
def do_network_delete(client, args):
    """ delete a virtual network """
    net = client.networks.delete(args.id)
    utils.print_dict(net)


#@utils.arg('id', metavar='<NETWORK_ID>', help='ID of network to synchronize config')
#def do_network_sync(client, args):
#    """ Synchronize the configuration of a virtual network """
#    try:
#        net = client.networks.perform_action(args.id, 'sync')
#        utils.print_dict(net)
#    except Exception as e:
#        utils.show_exception_and_exit(e)


@utils.arg('id', metavar='<NETWORK_ID>', help='ID of network to make public')
def do_network_public(client, args):
    """ Make a virtual network public """
    net = client.networks.perform_action(args.id, 'public')
    utils.print_dict(net)


@utils.arg('id', metavar='<NETWORK_ID>', help='ID of network to make private')
def do_network_private(client, args):
    """ Make a virtual network private """
    net = client.networks.perform_action(args.id, 'private')
    utils.print_dict(net)


@utils.arg('id', metavar='<NETWORK_ID>', help='ID of network to make private')
@utils.arg('--net', metavar='<DESTINATION>', action='append', help='Route destination prefix')
@utils.arg('--gw', metavar='<GATEWAY>', action='append', help='Route gateway')
def do_network_set_static_routes(client, args):
    """ Make a virtual network private """
    kwargs = {}
    if args.net and args.gw:
        if len(args.net) != len(args.gw):
            raise Exception('Inconsistent network and gateway pairs')
        routes = {}
        for i in range(len(args.net)):
            routes[args.net[i]] = args.gw[i]
        kwargs['static_routes'] = json.dumps(routes)
    else:
        kwargs['static_routes'] = None
    net = client.networks.set_metadata(args.id, **kwargs)
    utils.print_dict(net)


@utils.arg('id', metavar='<NETWORK_ID>', help='ID of network to swap IP address')
@utils.arg('node1', metavar='<NODE_ID>', help='ID of a VM or group')
@utils.arg('node2', metavar='<NODE_ID>', help='ID of a VM or group')
@utils.arg('--node1-type', metavar='<NODE_TYPE>', choices=['server', 'group'], help='Type of node1, either server or group')
@utils.arg('--node2-type', metavar='<NODE_TYPE>', choices=['server', 'group'], help='Type of node2, either server or group')
def do_network_swap_address(client, args):
    """ Swap IP address between virtual server or group """
    kwargs = {'node1': args.node1,
                'node2': args.node2}
    if args.node1_type:
        kwargs['node1_type'] = args.node1_type
    if args.node2_type:
        kwargs['node2_type'] = args.node2_type
    net = client.networks.perform_action(args.id, 'swap-address', **kwargs)
    utils.print_dict(net)


@utils.arg('id', metavar='<NETWORK_ID>', help='ID of network to update')
@utils.arg('dns', metavar='<DNS_SERVER>', help='DNS server address')
@utils.arg('key', metavar='<DNS_UPDATE_KEY>', help='DNS update key name')
@utils.arg('secret', metavar='<DNS_UPDATE_SECRET>', help='DNS update key secret')
def do_network_add_dns_update_target(client, args):
    """ Add a dns update target to a network """
    kwargs = {'server': args.dns}
    kwargs['key'] = args.key
    kwargs['secret'] = args.secret
    net = client.networks.perform_action(args.id, 'add-dns-update-target',
                                        **kwargs)
    utils.print_dict(net)


@utils.arg('id', metavar='<NETWORK_ID>', help='ID of network to update')
@utils.arg('dns', metavar='<DNS_SERVER>', help='DNS server address')
@utils.arg('key', metavar='<DNS_UPDATE_KEY>', help='DNS update key name')
def do_network_remove_dns_update_target(client, args):
    """ Remove a dns update target from a network """
    kwargs = {'server': args.dns, 'key': args.key}
    net = client.networks.perform_action(args.id, 'remove-dns-update-target',
                                        **kwargs)
    utils.print_dict(net)


@utils.arg('id', metavar='<NETWORK_ID>', help='ID of network to update')
@utils.arg('ip', metavar='<IPADDR>', help='IP address to reserve')
@utils.arg('--notes', metavar='<NOTES>', help='Notes')
def do_network_reserve_ip(client, args):
    """ Reserve an IP address from pool """
    kwargs = {'ip': args.ip}
    if args.notes:
        kwargs['notes'] = args.notes
    net = client.networks.perform_action(args.id, 'reserve-ip', **kwargs)
    utils.print_dict(net)


@utils.arg('id', metavar='<NETWORK_ID>', help='ID of network to update')
@utils.arg('ip', metavar='<IPADDR>', help='IP address to reserve')
def do_network_release_reserved_ip(client, args):
    """ Release a reserved IP into pool """
    net = client.networks.perform_action(args.id, 'release-reserved-ip',
                                            ip=args.ip)
    utils.print_dict(net)


@utils.arg('id', metavar='<NETWORK_ID>', help='ID of network to update')
def do_network_reserved_ips(client, args):
    """ Show all reserved IPs """
    net = client.networks.get_specific(args.id, 'reserved-ips')
    utils.print_dict(net)


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_reserved_ip_list(client, args):
    """ Show all reserved IPs for any network """
    page_info = utils.get_paging_info(args)
    ips = client.reservedips.list(**page_info)
    utils.print_list(ips, client.reservedips.columns)
