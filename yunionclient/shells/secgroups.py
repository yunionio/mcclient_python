from yunionclient.common import utils


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--admin', action='store_true', help='Is admin call?')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant ID or Name')
def do_secgroup_list(client, args):
    """ List all security group """
    page_info = utils.get_paging_info(args)
    sgs = client.secgroups.list(**page_info)
    utils.print_list(sgs, client.secgroups.columns)


@utils.arg('name', metavar='<NAME>', help='Name of security group to create')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
@utils.arg('--rule', metavar='<RULE>', action='append', required=True, help='security rule to remove')
def do_secgroup_create(client, args):
    """ Create a security group """
    kwargs = {}
    kwargs['name'] = args.name
    if args.desc is not None:
        kwargs['description'] = args.desc
    kwargs.update(parse_secgroup_rules(args))
    sg = client.secgroups.create(**kwargs)
    utils.print_dict(sg)


@utils.arg('id', metavar='<ID>', help='ID of security group to show')
def do_secgroup_show(client, args):
    """ Show details of a security group """
    sg = client.secgroups.get(args.id)
    utils.print_dict(sg)


@utils.arg('id', metavar='<ID>', help='ID of security group to show')
@utils.arg('--name', metavar='<NAME>', help='Name of security group to create')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
def do_secgroup_update(client, args):
    """ Update details of a security group """
    kwargs = {}
    if args.name:
        kwargs['name'] = args.name
    if args.desc is not None:
        kwargs['description'] = args.desc
    if len(kwargs) == 0:
        raise Exception('No data to update')
    sg = client.secgroups.update(args.id, **kwargs)
    utils.print_dict(sg)


@utils.arg('id', metavar='<ID>', help='ID of security group to delete')
def do_secgroup_delete(client, args):
    """ Delete a security group """
    sg = client.secgroups.delete(args.id)
    utils.print_dict(sg)


@utils.arg('id', metavar='<ID>', help='ID of security group')
def do_secgroup_public(client, args):
    """ Make a security group publicly available """
    sg = client.secgroups.perform_action(args.id, 'public')
    utils.print_dict(sg)


@utils.arg('id', metavar='<ID>', help='ID of security group')
def do_secgroup_private(client, args):
    """ Make a security group private """
    sg = client.secgroups.perform_action(args.id, 'private')
    utils.print_dict(sg)


def parse_secgroup_rules(args):
    kwargs = {}
    if args.rule and len(args.rule) > 0:
        idx = 0
        for r in args.rule:
            kwargs['rule.%d' % idx] = r
            idx += 1
    return kwargs


@utils.arg('id', metavar='<ID>', help='ID of security group to modify')
@utils.arg('--rule', metavar='<RULE>', action='append', help='security rule to add')
def do_secgroup_add_rules(client, args):
    """ Add security rules to a security group """
    kwargs = parse_secgroup_rules(args)
    if len(kwargs) == 0:
        raise Exception('No rule to add')
    sg = client.secgroups.perform_action(args.id, 'add-rules', **kwargs)
    utils.print_dict(sg)


@utils.arg('id', metavar='<ID>', help='ID of security group to modify')
@utils.arg('--rule', metavar='<RULE>', action='append', help='security rule to remove')
def do_secgroup_remove_rules(client, args):
    """ Remove security rules from a security group """
    kwargs = parse_secgroup_rules(args)
    if len(kwargs) == 0:
        raise Exception('No rule to remove')
    sg = client.secgroups.perform_action(args.id, 'remove-rules', **kwargs)
    utils.print_dict(sg)

@utils.arg('id', metavar='<ID>', help='ID of security group to modify')
@utils.arg('--rule', metavar='<RULE>', action='append', help='security rule to set')
def do_secgroup_set_rules(client, args):
    """ Set security rules from a security group """
    kwargs = parse_secgroup_rules(args)
    if len(kwargs) == 0:
        raise Exception('No rule to set')
    sg = client.secgroups.perform_action(args.id, 'set-rules', **kwargs)
    utils.print_dict(sg)
