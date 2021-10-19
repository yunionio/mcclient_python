from yunionclient.common import utils

@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--meta', action='store_true', help='Piggyback metadata')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--admin', action='store_true', help='Is admin call?')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant ID or Name')
@utils.arg('--user', metavar='<USER>', help='User ID or Name')
@utils.arg('--system', action='store_true', help='Show system objects?')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_server_sku_list(client, args):
    """ List server skus """
    page_info = utils.get_paging_info(args)
    skus = client.serverskus.list(**page_info)
    utils.print_list(skus, client.serverskus.columns)

@utils.arg('id', metavar='<DISK_ID>', help='ID of sku to show')
def do_server_sku_show(client, args):
    """ Show details of a server sku """
    sku = client.serverskus.get(args.id)
    utils.print_dict(sku)




