from yunionclient.common import utils


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to show')
@utils.arg('--since', metavar='<DATETIME>', help='Show logs since specific date')
@utils.arg('--until', metavar='<DATETIME>', help='Show logs until specific date')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Limit number of logs')
@utils.arg('--offset', metavar='<OFFSET>', help='OFFSET')
@utils.arg('--ascending', action='store_true', help='Ascending order or descending order')
@utils.arg('--action', metavar='<ACTION>', action='append', help='Action of log')
def do_server_event(client, args):
    """ Show operation events of a virtual server """
    args.type = 'server'
    do_event_show(client, args)

@utils.arg('id', metavar='<HOST_ID>', help='ID of host to show')
@utils.arg('--since', metavar='<DATETIME>', help='Show logs since specific date')
@utils.arg('--until', metavar='<DATETIME>', help='Show logs until specific date')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Limit number of logs')
@utils.arg('--offset', metavar='<OFFSET>', help='OFFSET')
@utils.arg('--ascending', action='store_true', help='Ascending order or descending order')
@utils.arg('--action', metavar='<ACTION>', action='append', help='Action of log')
def do_host_event(client, args):
    """ Show operation events of a virtual server """
    args.type = 'host'
    do_event_show(client, args)


@utils.arg('id', metavar='<HOST_ID>', help='ID of host to show')
@utils.arg('--since', metavar='<DATETIME>', help='Show logs since specific date')
@utils.arg('--until', metavar='<DATETIME>', help='Show logs until specific date')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Limit number of logs')
@utils.arg('--offset', metavar='<OFFSET>', help='OFFSET')
@utils.arg('--ascending', action='store_true', help='Ascending order or descending order')
@utils.arg('--action', metavar='<ACTION>', action='append', help='Action of log')
def do_zone_event(client, args):
    """ Show operation events of a virtual server """
    args.type = 'zone'
    do_event_show(client, args)


@utils.arg('id', metavar='<HOST_ID>', help='ID of host to show')
@utils.arg('--since', metavar='<DATETIME>', help='Show logs since specific date')
@utils.arg('--until', metavar='<DATETIME>', help='Show logs until specific date')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Limit number of logs')
@utils.arg('--offset', metavar='<OFFSET>', help='OFFSET')
@utils.arg('--ascending', action='store_true', help='Ascending order or descending order')
@utils.arg('--action', metavar='<ACTION>', action='append', help='Action of log')
def do_disk_event(client, args):
    """ Show operation events of a virtual server """
    args.type = 'disk'
    do_event_show(client, args)


@utils.arg('id', metavar='<BAREMETAL_ID>', help='ID of baremetal to show')
@utils.arg('--since', metavar='<DATETIME>', help='Show logs since specific date')
@utils.arg('--until', metavar='<DATETIME>', help='Show logs until specific date')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Limit number of logs')
@utils.arg('--offset', metavar='<OFFSET>', help='OFFSET')
@utils.arg('--ascending', action='store_true', help='Ascending order or descending order')
@utils.arg('--action', metavar='<ACTION>', action='append', help='Action of log')
def do_baremetal_event(client, args):
    """ Show operation events of a baremetal """
    args.type = 'baremetal'
    do_event_show(client, args)


@utils.arg('id', metavar='<BAREMETAL_ID>', help='ID of baremetal to show')
@utils.arg('--since', metavar='<DATETIME>', help='Show logs since specific date')
@utils.arg('--until', metavar='<DATETIME>', help='Show logs until specific date')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Limit number of logs')
@utils.arg('--offset', metavar='<OFFSET>', help='OFFSET')
@utils.arg('--ascending', action='store_true', help='Ascending order or descending order')
def do_baremetal_event(client, args):
    """ Show operation events of a virtual server """
    args.type = 'baremetal'
    do_event_show(client, args)


@utils.arg('--type', metavar='<OBJ_ID>', action='append', help='Type of relevant object')
@utils.arg('--id', metavar='<OBJ_ID>', help='ID of relevant object')
@utils.arg('--since', metavar='<DATETIME>', help='Show logs since specific date')
@utils.arg('--until', metavar='<DATETIME>', help='Show logs until specific date')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Limit number of logs')
@utils.arg('--offset', metavar='<OFFSET>', help='OFFSET')
@utils.arg('--ascending', action='store_true', help='Ascending order or descending order')
@utils.arg('--action', metavar='<ACTION>', action='append', help='Action of log')
def do_event_show(client, args):
    """ Show operation events of a virtual server """
    kwargs = {}
    if args.type is not None:
        kwargs['obj_type'] = args.type
    if args.id is not None:
        kwargs['obj_id']   = args.id
    if args.since is not None:
        kwargs['since'] = args.since
    if args.until is not None:
        kwargs['until'] = args.until
    if args.limit and int(args.limit) > 0:
        kwargs['limit'] = int(args.limit)
        if args.offset and int(args.offset) > 0:
            kwargs['offset'] = int(args.offset)
    if args.ascending:
        kwargs['order'] = 'asc'
    if args.action is not None:
        kwargs['action'] = args.action
    logs = client.logs.list(**kwargs)
    utils.print_list(logs, client.logs.columns)
