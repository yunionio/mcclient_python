from yunionclient.common import utils


def do_role_list(client, args):
    """ List keystone roles """
    rlist = client.roles.list()
    utils.print_list(rlist, client.roles.columns)


@utils.arg('name', metavar='<Name>', help='Role name')
def do_role_create(client, args):
    """ Create a keystone tenant """
    kwargs = {}
    kwargs['name'] = args.name
    role = client.roles.create(**kwargs)
    utils.print_dict(role)


@utils.arg('id', metavar='<ID>', help='Role ID')
def do_role_delete(client, args):
    """ Delete a keystone role """
    r = client.roles.get(args.id)
    client.roles.delete(r['id'])
