from yunionclient.common import utils


@utils.arg('--limit', metavar='<NUMBER>', type=int, default=20, help='Page limit')
def do_tenant_list(client, args):
    """ List keystone users """
    kwargs = {}
    if args.limit:
        kwargs['limit'] = args.limit
    tlist = client.tenants.list(**kwargs)
    utils.print_list(tlist, client.tenants.columns)


@utils.arg('id', metavar='<ID>', help='Tenant ID')
def do_tenant_show(client, args):
    """ Show details of keystone tenant """
    tenant = client.tenants.get(args.id)
    utils.print_dict(tenant)


@utils.arg('id', metavar='<ID>', help='Tenant ID')
@utils.arg('--name', metavar='<Name>', help='Tenant ID')
@utils.arg('--enabled', metavar='<BOOLEAN>', help='True or False')
def do_tenant_update(client, args):
    """ Show details of keystone tenant """
    t = client.tenants.get(args.id)
    kwargs = {}
    if args.name:
        kwargs['name'] = args.name
    if args.enabled:
        kwargs['enabled'] = utils.string_to_boolean(args.enabled)
    if len(kwargs) == 0:
        raise Exception('No data to update')
    client.tenants.update(t['id'], **kwargs)


@utils.arg('name', metavar='<Name>', help='Tenant name')
def do_tenant_create(client, args):
    """ Show details of keystone tenant """
    kwargs = {}
    kwargs['name'] = args.name
    tenant = client.tenants.create(**kwargs)
    utils.print_dict(tenant)


@utils.arg('id', metavar='<ID>', help='Tenant ID')
def do_tenant_delete(client, args):
    """ Delete a keystone tenant """
    t = client.tenants.get(args.id)
    client.tenants.delete(t['id'])


@utils.arg('id', metavar='<ID>', help='Tenant ID')
def do_tenant_user_list(client, args):
    """ List users in a keystone tenant """
    t = client.tenants.get(args.id)
    ulist = client.tenants.list_users(t['id'])
    utils.print_list(ulist, client.users.columns)
