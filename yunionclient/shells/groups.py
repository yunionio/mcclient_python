from yunionclient.common import utils


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--meta', action='store_true', help='Piggyback metadata')
@utils.arg('--admin', action='store_true', help='Is admin call?')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant ID or Name')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_group_list(client, args):
    """ List groups """
    page_info = utils.get_paging_info(args)
    groups = client.groups.list(**page_info)
    utils.print_list(groups, client.groups.columns)


@utils.arg('name', metavar='<GROUP_NAME>', help='Name of group to create')
@utils.arg('--desc', metavar='<GROUP_DESCRIPTION>', help='Description')
@utils.arg('--service-type', metavar='<GROUP_SERVICE_TYPE>', help='Service type of the guest group')
@utils.arg('--parent', metavar='<PARENT_GROUP>', help='Parent group ID or name')
@utils.arg('--zone', metavar='<GROUP_ZONE>', help='Zone')
@utils.arg('--scheduler-hint-memory', metavar='<MEMORY>', type=int, help='Memory of each virtual server in this group for schedulering hint')
@utils.arg('--scheduler-hint-exit-network', action='store_true', help='Wether each virtual server in this group owns an exit network interface')
@utils.arg('--scheduler-hint-max-count', metavar='<COUNT>', type=int, help='How many virtual servers will be in this group')
@utils.arg('--scheduler-hint-disk-size', metavar='<DISK_SIZE>', type=int, help='Disk size of each virtual server')
@utils.arg('--sched-strategy', metavar='<SCHED_STRATEGY>', type=str, help='Aggregate host strategy that has effects on scheduling result')
@utils.arg('--system', action='store_true', help='Create a system group, sysadmin ONLY option')
@utils.arg('--tenant', metavar='<TENANT>', help='Owner tenant ID or Name')
@utils.arg('--user', metavar='<USER>', help='Owner user ID or Name')
def do_group_create(client, args):
    """ Create a guest group (VM cluster) """
    kwargs = {}
    kwargs['name'] = args.name
    if args.desc is not None:
        kwargs['description'] = args.desc
    if args.service_type is not None:
        kwargs['service_type'] = args.service_type
    if args.parent is not None:
        kwargs['parent'] = args.parent
    if args.zone:
        kwargs['zone'] = args.zone
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.user:
        kwargs['user'] = args.user
    if args.scheduler_hint_memory:
        kwargs['sched_hint_memory'] = args.scheduler_hint_memory
    if args.scheduler_hint_exit_network:
        kwargs['sched_hint_exit_network'] = True
    if args.scheduler_hint_max_count:
        kwargs['sched_hint_max_count'] = args.scheduler_hint_max_count
    if args.scheduler_hint_disk_size:
        kwargs['sched_hint_disk_size'] = args.scheduler_hint_disk_size
    if args.system:
        kwargs['is_system'] = True
    if args.sched_strategy:
        kwargs['sched_strategy'] = args.sched_strategy
    group = client.groups.create(**kwargs)
    utils.print_dict(group)


@utils.arg('id', metavar='<GROUP_ID>', help='ID of group to delete')
def do_group_delete(client, args):
    """ Delete a guest group """
    group = client.groups.delete(args.id)
    utils.print_dict(group)


@utils.arg('id', metavar='<GROUP_ID>', help='ID of group to updae')
@utils.arg('--name', metavar='<GROUP_NAME>', help='Name of group to create')
@utils.arg('--desc', metavar='<GROUP_DESCRIPTION>', help='Description')
@utils.arg('--service-type', metavar='<GROUP_SERVICE_TYPE>', help='Service type of the guest group')
@utils.arg('--parent', metavar='<PARENT_GROUP>', help='Parent group ID or name')
@utils.arg('--sched-strategy', metavar='<SCHED_STRATEGY>', type=str, help='Aggregate host strategy that has effects on scheduling result')
def do_group_update(client, args):
    """ Update a guest group """
    kwargs = {}
    if args.name is not None:
        kwargs['name'] = args.name
    if args.desc is not None:
        kwargs['description'] = args.desc
    if args.service_type is not None:
        kwargs['service_type'] = args.service_type
    if args.parent is not None:
        kwargs['parent'] = args.parent
    if args.sched_strategy:
        kwargs['sched_strategy'] = args.sched_strategy
    if len(kwargs) == 0:
        raise Exception("No data", "No data to update")
    group = client.groups.update(args.id, **kwargs)
    utils.print_dict(group)


@utils.arg('id', metavar='<GROUP_ID>', help='ID of virtual group to get metadata info')
@utils.arg('--field', metavar='<METADATA_FIELD>', help='Field name of metadata')
def do_group_metadata(client, args):
    """ Show metadata info of a virtual server group """
    kwargs = {}
    if args.field is not None:
        kwargs['field'] = args.field
    group = client.groups.get_metadata(args.id, **kwargs)
    if isinstance(group, dict):
        utils.print_dict(group)
    else:
        print(group)


@utils.arg('id', metavar='<SERVER>', help='ID of virtual server')
@utils.arg('--group', metavar='<GROUP>', required=True, help='ID of group to join')
@utils.arg('--tag', metavar='<TAG>', help='Tag for this relationship')
def do_server_join_group(client, args):
    """ Join a virtual server into a group """
    if args.tag and len(args.tag) > 0:
        tag = args.tag
    else:
        tag = None
    groupguest = client.groupguests.attach(args.group, args.id, tag=tag)
    utils.print_dict(groupguest)


@utils.arg('id', metavar='<SERVER>', help='ID of virtual server')
@utils.arg('--group', metavar='<GROUP>', required=True, help='ID of group to join')
def do_server_leave_group(client, args):
    """ A virtual server leave a group """
    groupguest = client.groupguests.detach(args.group, args.id)
    utils.print_dict(groupguest)


@utils.arg('--group', metavar='<GROUP>', help='ID of group to join')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--admin', action='store_true', help='Is admin call?')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant ID or Name')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_group_server_list(client, args):
    """ List group-server relationship of all or given group """
    page_info = utils.get_paging_info(args)
    if args.group is not None:
        groupguests = client.groupguests.list_descendent(args.group,
                                                                **page_info)
    else:
        groupguests = client.groupguests.list(**page_info)
    utils.print_list(groupguests, client.groupguests.columns)


@utils.arg('id', metavar='<GROUP>', help='ID of group')
@utils.arg('--server', metavar='<SERVER>', required=True, help='ID of virtual server')
@utils.arg('--tag', metavar='<TAG>', help='Relationship tag', action='append')
@utils.arg('--action', metavar='<ACTION>', choices=['append', 'replace', 'remove'], help='Update action')
def do_group_server_updatetag(client, args):
    """ List group-server relationship of all or given group """
    kwargs = {}
    if args.tag is not None:
        idx = 0
        for t in args.tag:
            kwargs['tag.%d' % idx] = t
            idx += 1
    if args.action is not None:
        kwargs['action'] = args.action
    if len(kwargs) == 0:
        raise Exception('No data to update')
    groupguest = client.groupguests.update(args.id, args.server, **kwargs)
    utils.print_dict(groupguest)


@utils.arg('id', metavar='<GROUP>', help='ID of group')
@utils.arg('--server', metavar='<SERVER>', required=True, help='ID of virtual server')
def do_group_server_show(client, args):
    """ Show detail of group-server relationship """
    groupguest = client.groupguests.get(args.id, args.server)
    utils.print_dict(groupguest)


@utils.arg('id', metavar='<GROUP>', help='ID of group, or [all] for all groups')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--admin', action='store_true', help='Is admin call?')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant ID or Name')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_group_network_list(client, args):
    """ List all virtual networks of a virtual group """
    page_info = utils.get_paging_info(args)
    if args.id != 'all':
        groupnetworks = client.groupnetworks.list_descendent(args.id,
                                                                **page_info)
    else:
        groupnetworks = client.groupnetworks.list(**page_info)
    utils.print_list(groupnetworks, client.groupnetworks.columns)


@utils.arg('id', metavar='<GROUP>', help='ID of virtual group')
@utils.arg('--net', metavar='<NETWORK_DESC>', help='ID of virtual network')
@utils.arg('--port-count', metavar='<PORT_COUNT>', help='Number of virtual ports')
def do_group_network_attach(client, args):
    """ Attach a virtual network to a virtual group """
    kwargs = {}
    if args.net:
        kwargs['net_desc'] = args.net
    if args.port_count:
        kwargs['port_count'] = int(args.port_count)
    group = client.groups.perform_action(args.id, 'attachnetwork', **kwargs)
    utils.print_dict(group)


@utils.arg('id', metavar='<GROUP>', help='ID of virtual group')
def do_group_network_detach(client, args):
    """ Detach the virtual network fron a virtual group """
    group = client.groups.perform_action(args.id, 'detachnetwork')
    utils.print_dict(group)


@utils.arg('id', metavar='<GROUP>', help='ID of virtual group')
@utils.arg('--eip', metavar='<EIP>', help='EIP address')
def do_group_eip_add(client, args):
    """ Request an EIP to the virtual network of a virtual group """
    kwargs = {}
    if args.eip:
        kwargs['eip'] = args.eip
    group = client.groups.perform_action(args.id, 'addeip', **kwargs)
    utils.print_dict(group)


@utils.arg('id', metavar='<GROUP>', help='ID of virtual group')
@utils.arg('--eip', metavar='<EIP>', help='EIP address')
def do_group_eip_remove(client, args):
    """ Remove all or specified EIPs from a virtual group """
    kwargs = {}
    if args.eip:
        kwargs['eip'] = args.eip
    group = client.groups.perform_action(args.id, 'deleip', **kwargs)
    utils.print_dict(group)
