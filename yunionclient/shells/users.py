from yunionclient.common import utils


def do_user_list(client, args):
    """ List keystone users """
    ulist = client.users.list()
    utils.print_list(ulist, client.users.columns)


@utils.arg('id', metavar='<ID>', help='User ID')
def do_user_show(client, args):
    """ Show details of keystone user """
    user = client.users.get(args.id)
    utils.print_dict(user)


@utils.arg('name', metavar='<NAME>', help='User Name')
@utils.arg('--passwd', metavar='<PASSWORD>', required=True, help='Password')
@utils.arg('--tenant', metavar='<TENANT>', required=True, help='Default tenant')
@utils.arg('--email', metavar='<EMAIL>', help='Email')
@utils.arg('--mobile', metavar='<MOBILE>', help='Mobile')
@utils.arg('--enabled', metavar='<BOOLEAN>', help='Enabled or disabled')
def do_user_create(client, args):
    """ Create a keystone user """
    kwargs = {}
    kwargs['name'] = args.name
    kwargs['password'] = args.passwd
    t = client.tenants.get(args.tenant)
    kwargs['tenantId'] = t['id']
    if args.email:
        kwargs['email'] = args.email
    else:
        kwargs['email'] = ''
    if args.mobile:
        kwargs['mobile'] = args.mobile
    if args.enabled:
        kwargs['enabled'] = utils.string_to_boolean(args.enabled)
    else:
        kwargs['enabled'] = True
    user = client.users.create(**kwargs)
    utils.print_dict(user)


@utils.arg('id', metavar='<ID>', help='User ID or Name')
def do_user_delete(client, args):
    """ Delete a keystone user """
    u = client.users.get(args.id)
    client.users.delete(u['id'])


@utils.arg('id', metavar='<ID>', help='User ID or Name')
@utils.arg('--name', metavar='<NAME>', help='User Name')
@utils.arg('--tenant', metavar='<TENANT>', help='Default tenant')
@utils.arg('--email', metavar='<EMAIL>', help='Email')
@utils.arg('--mobile', metavar='<MOBILE>', help='Mobile')
@utils.arg('--enabled', metavar='<BOOLEAN>', help='Enabled or disabled')
@utils.arg('--extra', metavar='<EXTRA>', action='append', help='Extra info key:value')
def do_user_update(client, args):
    """ Update a keystone user """
    u = client.users.get(args.id)
    kwargs = {}
    if args.name:
        kwargs['name'] = args.name
    if args.tenant:
        t = client.tenants.get(args.tenant)
        kwargs['tenantId'] = t['id']
    if args.email:
        kwargs['email'] = args.email
    if args.mobile:
        kwargs['mobile'] = args.mobile
    if args.enabled:
        kwargs['enabled'] = utils.string_to_boolean(args.enabled)
    if args.extra:
        for ext in args.extra:
            if ext.count(':') != 1:
                raise Exception('Extra data not in format key:value')
            key, val = ext.split(':')
            if key in kwargs:
                raise Exception('Duplicate key %s' % key)
            kwargs[key] = val
    if len(kwargs) == 0:
        raise Exception('No data to update')
    client.users.update(u['id'], **kwargs)


@utils.arg('id', metavar='<ID>', help='User ID or Name')
@utils.arg('--passwd', required=True, metavar='<PASSWORD>', help='New password')
def do_user_password(client, args):
    """ Update password of a keystone user.
        Password setting to None in old version keystone would result in bugs.
    """
    u = client.users.get(args.id)
    client.users.update_password(u['id'], args.passwd)


@utils.arg('id', metavar='<ID>', help='User ID or Name')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant ID or Name')
def do_user_role_list(client, args):
    """ Get roles of a keystone user """
    u = client.users.get(args.id)
    if args.tenant:
        t = client.tenants.get(args.tenant)
        tid = t['id']
    else:
        tid = None
    rlist = client.users.roles_for_user(u['id'], tid=tid)
    utils.print_list(rlist, client.roles.columns)


@utils.arg('id', metavar='<USER>', help='User ID or Name')
@utils.arg('role', metavar='<ROLE>', help='Role')
@utils.arg('tenant', metavar='<TENANT>', help='Tenant ID or Name')
def do_user_role_add(client, args):
    """ Get roles of a keystone user """
    u = client.users.get(args.id)
    r = client.roles.get(args.role)
    if args.tenant:
        t = client.tenants.get(args.tenant)
        tid = t['id']
    else:
        tid = None
    u = client.users.add_role(u['id'], r['id'], tid=tid)
    utils.print_dict(u)


@utils.arg('id', metavar='<USER>', help='User ID or Name')
@utils.arg('role', metavar='<ROLE>', help='Role')
@utils.arg('tenant', metavar='<TENANT>', help='Tenant ID or Name')
def do_user_role_remove(client, args):
    """ Get roles of a keystone user """
    u = client.users.get(args.id)
    r = client.roles.get(args.role)
    if args.tenant:
        t = client.tenants.get(args.tenant)
        tid = t['id']
    else:
        tid = None
    client.users.remove_role(u['id'], r['id'], tid=tid)


@utils.arg('id', metavar='<USER>', help='User ID or Name')
def do_user_ec2_list(client, args):
    """ Get ec2 credential of a keystone user """
    u = client.users.get(args.id)
    ulist = client.ec2credentials.list_ec2cred(u['id'])
    utils.print_list(ulist, client.ec2credentials.columns)


@utils.arg('id', metavar='<USER>', help='User ID or Name')
@utils.arg('tenant', metavar='<TENANT>', help='Tenant ID or Name')
def do_user_ec2_create(client, args):
    """ Create ec2 credential of a keystone user """
    u = client.users.get(args.id)
    t = client.tenants.get(args.tenant)
    cred = client.ec2credentials.create_ec2cred(u['id'], t['id'])
    utils.print_dict(cred)


@utils.arg('id', metavar='<USER>', help='User ID or Name')
@utils.arg('access', metavar='<ACCESS>', help='EC2 credential access ID')
def do_user_ec2_show(client, args):
    """ Show details of an ec2 credential of a keystone user """
    u = client.users.get(args.id)
    cred = client.ec2credentials.get_ec2cred(u['id'], args.access)
    utils.print_dict(cred)


@utils.arg('id', metavar='<USER>', help='User ID or Name')
@utils.arg('access', metavar='<ACCESS>', help='EC2 credential access ID')
def do_user_ec2_delete(client, args):
    """ Delete ec2 credential of a keystone user """
    u = client.users.get(args.id)
    client.ec2credentials.delete_ec2cred(u['id'], args.access)
