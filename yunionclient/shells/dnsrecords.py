from yunionclient.common import utils


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--admin', action='store_true', help='Is admin call?')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant ID or Name')
@utils.arg('--is-public', action='store_true', help='Show public records only')
def do_dns_list(client, args):
    """ List all dns records """
    page_info = utils.get_paging_info(args)
    if args.is_public:
        page_info['is_public'] = 1
    dns_list = client.dns.list(**page_info)
    utils.print_list(dns_list, client.dns.columns)


def parse_dns_arguments(args):
    kwargs = {}
    for type in ['A', 'AAAA']:
        recs = getattr(args, type, None)
        if recs is not None:
            idx = 0
            for r in recs:
                kwargs['%s.%d' % (type, idx)] = r
                idx += 1
    if hasattr(args, 'CNAME') and args.CNAME:
        if len(kwargs) > 0:
            raise Exception('CNAME cannot mix with other records')
        kwargs['CNAME'] = args.CNAME
    if hasattr(args, 'SRV_host') and hasattr(args, 'SRV_port') and \
            args.SRV_host and args.SRV_port:
        if len(kwargs) > 0:
            raise Exception('SRV cannot mix with other records')
        kwargs['SRV_host'] = args.SRV_host
        kwargs['SRV_port'] = args.SRV_port
    return kwargs


@utils.arg('name', metavar='<NAME>', help='Name of security group to create')
@utils.arg('--ttl', metavar='<TTL>', help='TTL in seconds')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
@utils.arg('--A', metavar='<A_RECORD>', action='append', help='DNS A record')
@utils.arg('--AAAA', metavar='<AAAA_RECORD>', action='append', help='DNS AAAA record')
@utils.arg('--CNAME', metavar='<CNAME_RECORD>', help='DNS CNAME record')
@utils.arg('--SRV-host', metavar='<SRV_RECORD_HOST>', help='DNS SRV record, server of service')
@utils.arg('--SRV-port', metavar='<SRV_RECORD_PORT>', help='DNS SRV record, port of service')
def do_dns_create(client, args):
    """ Create a dns record """
    kwargs = {}
    kwargs['name'] = args.name
    if args.ttl:
        kwargs['ttl'] = args.ttl
    if args.desc is not None:
        kwargs['description'] = args.desc
    kwargs.update(parse_dns_arguments(args))
    dns = client.dns.create(**kwargs)
    utils.print_dict(dns)


@utils.arg('id', metavar='<ID>', help='ID of DNS record to show')
def do_dns_show(client, args):
    """ Show details of a dns records """
    dns = client.dns.get(args.id)
    utils.print_dict(dns)


@utils.arg('id', metavar='<ID>', help='ID of DNS record to update')
@utils.arg('--name', metavar='<NAME>', help='Domain name')
@utils.arg('--ttl', metavar='<TTL>', help='TTL in seconds')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
def do_dns_update(client, args):
    """ Update details of a dns records """
    kwargs = {}
    if args.name:
        kwargs['name'] = args.name
    if args.ttl:
        kwargs['ttl'] = args.ttl
    if args.desc is not None:
        kwargs['description'] = args.desc
    if len(kwargs) == 0:
        raise Exception('No data to update')
    dns = client.dns.update(args.id, **kwargs)
    utils.print_dict(dns)


@utils.arg('id', metavar='<ID>', help='ID of DNS record to delete')
def do_dns_delete(client, args):
    """ Delete a dns record """
    dns = client.dns.delete(args.id)
    utils.print_dict(dns)


@utils.arg('id', metavar='<ID>', help='ID of dns record')
def do_dns_public(client, args):
    """ Make a dns record publicly available """
    dns = client.dns.perform_action(args.id, 'public')
    utils.print_dict(dns)


@utils.arg('id', metavar='<ID>', help='ID of dns record')
def do_dns_private(client, args):
    """ Make a dns record private """
    dns = client.dns.perform_action(args.id, 'private')
    utils.print_dict(dns)


@utils.arg('id', metavar='<ID>', help='ID of dns record to modify')
@utils.arg('--A', metavar='<A>', action='append', help='Type A dns record to add')
@utils.arg('--AAAA', metavar='<AAAA>', action='append', help='Type AAAA dns record to add')
@utils.arg('--SRV-host', metavar='<SRV_RECORD_HOST>', help='DNS SRV record, server of service')
@utils.arg('--SRV-port', metavar='<SRV_RECORD_PORT>', help='DNS SRV record, port of service')
def do_dns_add_records(client, args):
    """ Add DNS records to a dns name """
    kwargs = parse_dns_arguments(args)
    if len(kwargs) == 0:
        raise Exception('No record to add')
    dns = client.dns.perform_action(args.id, 'add-records', **kwargs)
    utils.print_dict(dns)


@utils.arg('id', metavar='<ID>', help='ID of DNS record to modify')
@utils.arg('--A', metavar='<A>', action='append', help='Type A dns record to add')
@utils.arg('--AAAA', metavar='<AAAA>', action='append', help='Type AAAA dns record to add')
@utils.arg('--SRV-host', metavar='<SRV_RECORD_HOST>', help='DNS SRV record, server of service')
@utils.arg('--SRV-port', metavar='<SRV_RECORD_PORT>', help='DNS SRV record, port of service')
def do_dns_remove_records(client, args):
    """ Remove DNS records from a domain name """
    kwargs = parse_dns_arguments(args)
    if len(kwargs) == 0:
        raise Exception('No records to remove')
    dns = client.dns.perform_action(args.id, 'remove-records', **kwargs)
    utils.print_dict(dns)


###############################DNSUPDATE#####################################

@utils.arg('domain_name', metavar='<DOMAIN_NAME>', help='domain name')
@utils.arg('--ip', metavar='<IP>', required=True, help='ip address')
@utils.arg('--dns-server-ip', metavar='<DNS_SRV_IP>', required=True, help='dns server ip')
@utils.arg('--key', metavar='<KEY>', required=True, help='key name')
@utils.arg('--secret', metavar='<KEY_SECRET>', required=True, help='key secret')
@utils.arg('--is-add', metavar='<IS_ADD>', help='True or False')
def do_dnsupdate(client, args):
    """ Update a server's nic dns record """
    kwargs = {}
    kwargs['guest_name'] = args.domain_name[:args.domain_name.find('.')]
    kwargs['guest_domain'] = args.domain_name[args.domain_name.find('.')+1:]
    kwargs['ip_addr'] = args.ip
    kwargs['guest_dns'] = args.dns_server_ip
    kwargs['key_name'] = args.key
    kwargs['key_secret'] = args.secret
    if args.is_add and args.is_add in ['False', 'false']:
        kwargs['is_add'] = False
    else:
        kwargs['is_add'] = True
    try:
        dnsupdate = client.dnsupdate.create(**kwargs)
    except Exception as err:
        raise Exception('dns update error: %s' % err)
    else:
        utils.print_dict(dnsupdate)


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--admin', action='store_true', help='Is admin call?')
@utils.arg('--user', metavar='<USER>', help='User ID or Name')
@utils.arg('--datetime', metavar='<DATETIME>', help='List notify info recorded after datetime<YYYY-MM-DD HH:MM:SS>')
def do_dnsupdate_request_list(client, args):
    """ List all notify request histories """
    page_info = utils.get_paging_info(args)
    if args.datetime is not None:
        page_info['datetime'] = args.datetime
    requests = client.dnsupdate.list(**page_info)
    utils.print_list(requests, client.dnsupdate.columns)
