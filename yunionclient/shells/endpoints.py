from yunionclient.common import utils
from yunionclient.common import exceptions

def do_endpoint_list(client, args):
    """ List keystone service endpoints """
    elist = client.endpoints.list()
    utils.print_list(elist, client.endpoints.columns)


@utils.arg('region', metavar='<REGION>', help='Endpoint region')
@utils.arg('service', metavar='<SERVICE>', help='Service ID or Name')
@utils.arg('--zone', metavar='<ZONE>', help='Endpoint Zone')
def do_endpoint_show(client, args):
    """ show a service endpoint in a region """
    s = client.services.get_by_id_or_name(args.service)
    e = client.endpoints.get_service_endpoint_in_region(s['id'], args.region,
                                                        args.zone)
    utils.print_dict(e)


@utils.arg('region', metavar='<REGION>', help='Endpoint region')
@utils.arg('service', metavar='<SERVICE>', help='Service ID or Name')
@utils.arg('url', metavar='<PUBLIC_URL>', help='Public access URL')
@utils.arg('--zone', metavar='<ZONE>', help='Zone name')
@utils.arg('--internal-url', metavar='<INTERNAL_URL>', help='Internal access URL')
@utils.arg('--admin-url', metavar='<ADMIN_URL>', help='Administrative access URL')
def do_endpoint_create(client, args):
    """ register a service endpoint in a region """
    s = client.services.get_by_id_or_name(args.service)
    try:
        client.endpoints.get_service_endpoint_in_region(s['id'], args.region,
                                                        args.zone)
        raise Exception('Service "%s" has an endpoint in region "%s/%s"' %
                                (s['name'], args.region, args.zone))
    except exceptions.NotFound:
        pass
    kwargs = {}
    if args.zone is not None:
        kwargs['region'] = '%s/%s' % (args.region, args.zone)
    else:
        kwargs['region'] = args.region
    kwargs['service_id'] = s['id']
    kwargs['publicurl'] = args.url
    if args.internal_url:
        kwargs['internalurl'] = args.internal_url
    else:
        kwargs['internalurl'] = args.url
    if args.admin_url:
        kwargs['adminurl'] = args.admin_url
    else:
        kwargs['adminurl'] = args.url
    endpoint = client.endpoints.create(**kwargs)
    utils.print_dict(endpoint)


@utils.arg('region', metavar='<REGION>', help='Endpoint region')
@utils.arg('service', metavar='<SERVICE>', help='Service ID or Name')
@utils.arg('--zone', metavar='<ZONE>', help='Zone name')
def do_endpoint_delete(client, args):
    """ Delete a service endpoint in a region """
    s = client.services.get_by_id_or_name(args.service)
    e = client.endpoints.get_service_endpoint_in_region(s['id'], args.region,
                                                        args.zone)
    client.endpoints.delete(e['id'])
