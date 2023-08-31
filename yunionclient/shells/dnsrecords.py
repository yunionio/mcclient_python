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

