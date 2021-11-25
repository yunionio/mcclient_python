import yunionclient

from yunionclient.common import utils

@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_dbinstance_network_list(client, args):
    """ List all dbinstance networks"""
    page_info = utils.get_paging_info(args)
    dns = client.dbinstancenetworks.list(**page_info)
    utils.print_list(dns, client.dbinstancenetworks.columns)


