from yunionclient.common import utils

@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
def do_schedtag_list(client, args):
    page_info = utils.get_paging_info(args)
    schedtags = client.schedtags.list(**page_info)
    utils.print_list(schedtags, client.schedtags.columns)


@utils.arg('id', metavar='<AGGREGATE>', help='ID or Name of an schedtag')
def do_schedtag_show(client, args):
    kwargs = {}
    kwargs['with_meta'] = True
    schedtag = client.schedtags.get(args.id, **kwargs)
    utils.print_dict(schedtag)


@utils.arg('id', metavar='<AGGREGATE>', help='ID or Name of an schedtag')
@utils.arg('--name', metavar='<AGGREGATE_NAME>', help='Name of an schedtag')
@utils.arg('--default_strategy', metavar='<DEFAULT_STRATEGY>', choices=['require', 'exclude', 'prefer', 'avoid'],
           help='Default strategy of the schedtag, value = require|exclude|prefer|avoid')
@utils.arg('--desc', metavar='<AGGREGATE_DESCRIPTION>', help='Description')
def do_schedtag_update(client, args):
    kwargs = {}
    if args.name is not None:
        kwargs['name'] = args.name
    if args.desc is not None:
        kwargs['description'] = args.desc
    if args.default_strategy:
        kwargs['default_strategy'] = args.default_strategy
    if len(kwargs) == 0:
        raise Exception("No data", "No data to update")
    schedtag = client.schedtags.update(args.id, **kwargs)
    utils.print_dict(schedtag)


@utils.arg('name', metavar='<AGGREGATE_NAME>', help='Name of schedtag to create')
@utils.arg('--default_strategy', metavar='<DEFAULT_STRATEGY>', choices=['require', 'exclude', 'prefer', 'avoid'],
           help='Default strategy of the schedtag, value = require|exclude|prefer|avoid')
@utils.arg('--desc', metavar='<AGGREGATE_DESCRIPTION>', help='Description')
def do_schedtag_create(client, args):
    kwargs = {}
    if args.name:
        kwargs['name'] = args.name
    if args.desc:
        kwargs['desc'] = args.desc
    if args.default_strategy:
        kwargs['default_strategy'] = args.default_strategy
    schedtag = client.schedtags.create(**kwargs)
    utils.print_dict(schedtag)


@utils.arg('id', metavar='<AGGREGATE>', help='ID or name of an schedtag')
def do_schedtag_delete(client, args):
    schedtag = client.schedtags.delete(args.id)
    utils.print_dict(schedtag)


@utils.arg('id', metavar='<AGGREGATE>', help='ID or Name of an schedtag')
@utils.arg('--data', metavar='<KEY:VALUE>', action='append', help='Key:Value')
def do_schedtag_update_metadata(client, args):
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
    schedtag = client.schedtags.set_metadata(args.id, **kwargs)
    utils.print_dict(schedtag)


@utils.arg('id', metavar='<all|AGGREGATE>', help='ID or name of the schedtag')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
def do_schedtag_host_list(client, args):
    page_info = utils.get_paging_info(args)
    if args.id != 'all':
        schedtag_hosts = client.schedtag_hosts.list_descendent(args.id, **page_info)

    else:
        schedtag_hosts = client.schedtag_hosts.list(**page_info)
    utils.print_list(schedtag_hosts, client.schedtag_hosts.columns)


@utils.arg('schedtag', metavar='<AGGREGATE>', help='ID or name of the schedtag')
@utils.arg('host', metavar='<HOST>', nargs='+', help='ID or name of the host')
def do_schedtag_host_add(client, args):
    for each_host in args.host:
        schedtag_host = client.schedtag_hosts.attach(args.schedtag, each_host)
        utils.print_dict(schedtag_host)


@utils.arg('schedtag', metavar='<AGGREGATE>', help='ID or name of the schedtag')
@utils.arg('host', metavar='<HOST>', help='ID or name of the host')
def do_schedtag_host_remove(client, args):
    schedtag_host = client.schedtag_hosts.detach(args.schedtag, args.host)
    utils.print_dict(schedtag_host)


@utils.arg('key', metavar='<KEY>', help='Key of schedtag property')
def do_schedtag_host_list_by_metadata(client, args):
    # Search sequence: metadata_key -> schedtag -> hosts
    target_agg_ids = []
    schedtags = client.schedtags.list(limit=0)
    if len(schedtags) > 0:
        schedtags = schedtags[0]
    for schedtag in schedtags:
        schedtag_detail = client.schedtags.get(schedtag['id'], with_meta=True)
        if 'metadata' in schedtag_detail:
            metadata = schedtag_detail['metadata']
            for k, v in metadata.items():
                if args.key == k:
                    target_agg_ids.append(schedtag['id'])
    for schedtag in target_agg_ids:
        schedtag_hosts = client.schedtag_hosts.list_descendent(schedtag, limit=0)
        utils.print_list(schedtag_hosts, client.schedtag_hosts.columns)
