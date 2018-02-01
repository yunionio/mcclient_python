from yunionclient.common import utils


def do_service_list(client, args):
    """ List keystone services """
    tlist = client.services.list()
    utils.print_list(tlist, client.services.columns)


@utils.arg('id', metavar='<ID>', help='Service ID or name')
def do_service_show(client, args):
    """ Show details of keystone service """
    s = client.services.get_by_id_or_name(args.id)
    utils.print_dict(s)


@utils.arg('name', metavar='<NAME>', help='Service name')
@utils.arg('type', metavar='<TYPE>', choices=['compute', 'identity', 'image', 'volume', 'network', 'object-store', 'ec2', 'object-stats', 'vncproxy', 'meter', 'elb', 'billing', 'notify', 'sshrelay', 'monitor', 'redis', 'netmap-proxy', 'status', 'rds', 'swiftmeter', 'dnsupdate', 'baremetal'], help='Service type')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Descriptions')
def do_service_create(client, args):
    """ Show details of keystone tenant """
    kwargs = {}
    kwargs['name'] = args.name
    kwargs['type'] = args.type
    if args.desc:
        kwargs['description'] = args.desc
    service = client.services.create(**kwargs)
    utils.print_dict(service)


@utils.arg('id', metavar='<ID>', help='Tenant ID')
def do_service_delete(client, args):
    """ Delete a keystone tenant """
    s = client.services.get_by_id_or_name(args.id)
    client.services.delete(s['id'])
