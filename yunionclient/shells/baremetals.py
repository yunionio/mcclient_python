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
def do_baremetal_agent_list(client, args):
    """ List Baremetal Agents """
    page_info = utils.get_paging_info(args)
    baremetalagents = client.baremetalagents.list(**page_info)
    utils.print_list(baremetalagents, client.baremetalagents.columns)


@utils.arg('name', metavar='<NAME>', help='Name of baremetal agent')
@utils.arg('access_ip', metavar='<ACCESS_IP>', help='Access IP')
@utils.arg('manager_uri', metavar='<MANAGER_URI>', help='Management API URI')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
def do_baremetal_agent_create(client, args):
    """ Create a baremetal agent """
    kwargs = {}
    kwargs['name'] = args.name
    kwargs['access_ip'] = args.access_ip
    kwargs['manager_uri'] = args.manager_uri
    if args.desc:
        kwargs['description'] = args.desc
    baremetalagent = client.baremetalagents.create(**kwargs)
    utils.print_dict(baremetalagent)


@utils.arg('id', metavar='<ID>', help='ID or Name of baremetal agent')
@utils.arg('--name', metavar='<NAME>', help='Name of baremetal agent')
@utils.arg('--access-ip', metavar='<ACCESS_IP>', help='Access IP')
@utils.arg('--manager-uri', metavar='<MANAGER_URI>', help='Management API URI')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
def do_baremetal_agent_update(client, args):
    """ Update a baremetal agent """
    kwargs = {}
    if args.name:
        kwargs['name'] = args.name
    if args.access_ip:
        kwargs['access_ip'] = args.access_ip
    if args.manager_uri:
        kwargs['manager_uri'] = args.manager_uri
    if args.desc:
        kwargs['description'] = args.desc
    if len(kwargs) == 0:
        raise Exception('No data to update')
    baremetalagent = client.baremetalagents.update(args.id, **kwargs)
    utils.print_dict(baremetalagent)


@utils.arg('id', metavar='<ID>', help='ID or Name of baremetal agent')
def do_baremetal_agent_show(client, args):
    """ Show details of a baremetal agent """
    baremetalagent = client.baremetalagents.get(args.id)
    utils.print_dict(baremetalagent)


@utils.arg('id', metavar='<ID>', help='ID or Name of baremetal agent')
def do_baremetal_agent_enable(client, args):
    """ Enable a baremetal agent """
    baremetalagent = client.baremetalagents.perform_action(args.id, 'enable')
    utils.print_dict(baremetalagent)


@utils.arg('id', metavar='<ID>', help='ID or Name of baremetal agent')
def do_baremetal_agent_disable(client, args):
    """ Disable a baremetal agent """
    baremetalagent = client.baremetalagents.perform_action(args.id, 'disable')
    utils.print_dict(baremetalagent)


@utils.arg('id', metavar='<ID>', help='ID or Name of baremetal agent')
def do_baremetal_agent_delete(client, args):
    """ Delete a baremetal agent """
    baremetalagent = client.baremetalagents.delete(args.id)
    utils.print_dict(baremetalagent)


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
@utils.arg('--agent', metavar='<AGENT>', help='Show baremetals managed by the specified agent')
def do_baremetal_list(client, args):
    """ List Baremetals """
    page_info = utils.get_paging_info(args)
    if args.agent:
        page_info['agent'] = args.agent
    baremetals = client.baremetals.list(**page_info)
    utils.print_list(baremetals, client.baremetals.columns)


@utils.arg('name', metavar='<NAME>', help='Name of baremetal')
@utils.arg('mac', metavar='<MAC>', help='Default MAC address of baremetal')
@utils.arg('--guid', metavar='<GUID>', help='PXE client GUID of baremetal')
@utils.arg('--rack', metavar='<RACK>', help='Rack number of baremetal')
@utils.arg('--slots', metavar='<SLOTS>', help='Slots number of baremetal')
#@utils.arg('--ipmi-user', metavar='<IPMI_USER>', help='IPMI user')
@utils.arg('--ipmi-passwd', metavar='<IPMI_PASSWD>', help='IPMI user password')
@utils.arg('--ipmi-addr', metavar='<IPMI_ADDR>', help='IPMI IP address')
def do_baremetal_create(client, args):
    """ Create a baremetal """
    kwargs = {}
    kwargs['name'] = args.name
    kwargs['access_mac'] = args.mac
    if args.guid:
        kwargs['cli_guid'] = args.guid
    if args.rack:
        kwargs['rack'] = args.rack
    if args.slots:
        kwargs['slots'] = args.slots
    # if args.ipmi_user:
    #     kwargs['ipmi_username'] = args.ipmi_user
    if args.ipmi_passwd:
        kwargs['ipmi_password'] = args.ipmi_passwd
    if args.ipmi_addr:
        kwargs['ipmi_ip_addr'] = args.ipmi_addr
    baremetal = client.baremetals.create(**kwargs)
    utils.print_dict(baremetal)


@utils.arg('id', metavar='<ID>', help='ID or name of baremetal')
@utils.arg('--name', metavar='<NAME>', help='Name of baremetal')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description of baremetal')
@utils.arg('--ncpu', metavar='<CPU_CORE_COUNT>', type=int, help='Num of CPU logical cores')
@utils.arg('--ncpu-nodes', metavar='<CPU_NODE_COUNT>', type=int, help='Number of CPU nodes')
@utils.arg('--cpu-mhz', metavar='<CPU_MHZ>', type=int, help='CPU Mhz')
@utils.arg('--cpu-desc', metavar='<CPU_DESC>', help='Description of CPU')
@utils.arg('--cpu-cache-size', metavar='<CPU_CACHE_KB>', help='CPU cache size in KiB')
@utils.arg('--mem-size', metavar='<MEMSIZE_MB>', help='Memory size in MB')
@utils.arg('--rack', metavar='<RACK>', help='Rack number of baremetal')
@utils.arg('--slots', metavar='<SLOTS>', help='Slots number of baremetal')
@utils.arg('--ipmi-ip', metavar='<IPMI_IP>', help='IPMI IP')
#@utils.arg('--ipmi-username', metavar='<IPMI_USERNAME>', help='IPMI username')
@utils.arg('--ipmi-password', metavar='<IPMI_PASSWORD>', help='IPMI password')
def do_baremetal_update(client, args):
    """ Update baremetal """
    kwargs = {}
    if args.name:
        kwargs['name'] = args.name
    if args.desc:
        kwargs['description'] = args.desc
    if args.ncpu:
        kwargs['cpu_count'] = args.ncpu
    if args.ncpu_nodes:
        kwargs['node_count'] = args.ncpu_nodes
    if args.cpu_mhz:
        kwargs['cpu_mhz'] = args.cpu_mhz
    if args.cpu_desc:
        kwargs['cpu_desc'] = args.cpu_desc
    if args.cpu_cache_size:
        kwargs['cpu_cache'] = args.cpu_cache_size
    if args.mem_size:
        kwargs['mem_size'] = args.mem_size
    if args.rack:
        kwargs['rack'] = args.rack
    if args.slots:
        kwargs['slots'] = args.slots
    if args.ipmi_ip:
        kwargs['ipmi_ip_addr'] = args.ipmi_ip
    # if args.ipmi_username:
    #     kwargs['ipmi_username'] = args.ipmi_username
    if args.ipmi_password:
        kwargs['ipmi_password'] = args.ipmi_password
    baremetal = client.baremetals.update(args.id, **kwargs)
    utils.print_dict(baremetal)


@utils.arg('id', metavar='<ID>', help='ID or name of baremetal')
def do_baremetal_show(client, args):
    """ Show details of baremetal """
    baremetal = client.baremetals.get(args.id)
    utils.print_dict(baremetal)


@utils.arg('id', metavar='<ID>', help='ID or name of baremetal')
def do_baremetal_delete(client, args):
    """ Delete a baremetal """
    baremetal = client.baremetals.delete(args.id)
    utils.print_dict(baremetal)


@utils.arg('id', metavar='<ID>', help='ID or name of baremetal')
@utils.arg('mac', metavar='<MAC>', help='Mac address of interface')
@utils.arg('--wire', metavar='<WIRE>', help='WIRE that this interface attach to')
@utils.arg('--type', metavar='<NIC_TYPE>', choices=['ipmi', 'admin', 'normal'], help='Type of net interface, either ipmi, admin or normal')
@utils.arg('--rate', metavar='<RATE>', type=int, choices=[1000, 10000], help='Rate of NIC, either 1000 or 10000 Mbps')
@utils.arg('--index', metavar='<INDEX>', type=int, help='Index of NIC')
def do_baremetal_add_netif(client, args):
    """ Add a network interface to a baremetal """
    kwargs = {'mac': args.mac}
    if args.wire:
        kwargs['wire'] = args.wire
    if args.type:
        kwargs['nic_type'] = args.type
    if args.rate:
        kwargs['rate'] = args.rate
    if args.index:
        kwargs['index'] = args.index
    info = client.baremetals.perform_action(args.id, 'add-netif', **kwargs)
    utils.print_dict(info)


@utils.arg('id', metavar='<ID>', help='ID or name of baremetal')
@utils.arg('mac', metavar='<MAC>', help='Mac address of interface')
def do_baremetal_remove_netif(client, args):
    """ Remove a network interface from a baremetal """
    info = client.baremetals.perform_action(args.id, 'remove-netif',
                                            mac=args.mac)
    utils.print_dict(info)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal, or [all] for all baremetals')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--admin', action='store_true', help='Is admin call?')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant ID or Name')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_baremetal_network_list(client, args):
    """ List all virtual networks of a baremetal """
    page_info = utils.get_paging_info(args)
    if args.id != 'all':
        baremetalnetworks = client.baremetalnetworks.list_descendent(args.id,
                                                                **page_info)
    else:
        baremetalnetworks = client.baremetalnetworks.list(**page_info)
    utils.print_list(baremetalnetworks, client.baremetalnetworks.columns)

@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal, or [all] for all baremetals')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--admin', action='store_true', help='Is admin call?')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant ID or Name')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_baremetal_storage_list(client, args):
    """ List all storages of a baremetal """
    page_info = utils.get_paging_info(args)
    if args.id != 'all':
        bss = client.baremetalstorages.list_descendent(args.id, **page_info)
    else:
        bss = client.baremetalstorages.list(**page_info)
    utils.print_list(bss, client.baremetalstorages.columns)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
@utils.arg('mac', metavar='<MAC>', help='MAC of network interface')
@utils.arg('--net', metavar='<NETWORK>', help='ID of preferred network')
@utils.arg('--ip-addr', metavar='<IP_ADDR>', help='Preferred IP address')
@utils.arg('--alloc-dir', metavar='<ALLOC_DIRECTION>', choices=['stepdown', 'stepup'], help='Allocation direction in address pool')
def do_baremetal_enable_netif(client, args):
    """ Enable a network interface of a baremetal """
    kwargs = {'mac': args.mac}
    if args.net:
        kwargs['network'] = args.net
    if args.ip_addr:
        kwargs['ip_addr'] = args.ip_addr
    if args.alloc_dir:
        kwargs['alloc_dir'] = args.alloc_dir
    obj = client.baremetals.perform_action(args.id, 'enable-netif', **kwargs)
    utils.print_dict(obj)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
@utils.arg('mac', metavar='<MAC>', help='MAC of netif')
def do_baremetal_disable_netif(client, args):
    """ Disable a network interface of a baremetal """
    obj = client.baremetals.perform_action(args.id, 'disable-netif',
                                                    mac=args.mac)
    utils.print_dict(obj)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
@utils.arg('capacity', metavar='<CAPACITY>', help='Capacity of storage')
def do_baremetal_update_storage(client, args):
    """ Update storage capacity of a baremetal """
    obj = client.baremetals.perform_action(args.id, 'update-storage',
                                                    capacity=args.capacity)
    utils.print_dict(obj)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
@utils.arg('--force-reboot', action='store_true', help='Force reboot baremetal')
def do_baremetal_maintenance(client, args):
    """ Put a baremetal into maintenance mode """
    kwargs = {}
    if args.force_reboot:
        kwargs['force_reboot'] = True
    obj = client.baremetals.perform_action(args.id, 'maintenance', **kwargs)
    utils.print_dict(obj)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
def do_baremetal_unmaintenance(client, args):
    """ Put a baremetal leave from the maintenance mode """
    obj = client.baremetals.perform_action(args.id, 'unmaintenance')
    utils.print_dict(obj)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
@utils.arg('--field', metavar='<METADATA_FIELD>', help='Field name of metadata')
def do_baremetal_metadata(client, args):
    """ Show metadata info of a baremetal """
    kwargs = {}
    if args.field is not None:
        kwargs['field'] = args.field
    obj = client.baremetals.get_metadata(args.id, **kwargs)
    if isinstance(obj, dict):
        utils.print_dict(obj)
    else:
        print(obj)

@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
def do_baremetal_vnc(client, args):
    """ Get baremetal vnc info """
    info = client.baremetals.get_specific(args.id, 'vnc')
    utils.print_dict(info)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
def do_baremetal_enable(client, args):
    """ Enable a baremetal """
    info = client.baremetals.perform_action(args.id, 'enable')
    utils.print_dict(info)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
def do_baremetal_disable(client, args):
    """ Enable a baremetal """
    info = client.baremetals.perform_action(args.id, 'disable')
    utils.print_dict(info)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
def do_baremetal_start(client, args):
    """ Start a baremetal """
    info = client.baremetals.perform_action(args.id, 'start')
    utils.print_dict(info)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
def do_baremetal_stop(client, args):
    """ Stop a baremetal """
    info = client.baremetals.perform_action(args.id, 'stop')
    utils.print_dict(info)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
def do_baremetal_reset(client, args):
    """ Reset a baremetal """
    info = client.baremetals.perform_action(args.id, 'reset')
    utils.print_dict(info)


@utils.arg('name', metavar='<SERVER_NAME>', help='Name of VM server')
@utils.arg('--flavor', metavar='<FLAVOR_ID>', help='ID of server flavor')
@utils.arg('--image', metavar='<ROOT_IMAGE_ID>', help='ID of root disk image')
@utils.arg('--guest-os', metavar='<OS>', choices=['windows', 'linux'], help='Guest OS type')
@utils.arg('--extra-ext-bandwidth', metavar='<BANDWIDTH>', help='Extra external bandwidth, default in Mbps')
@utils.arg('--extra-ext-disksize', metavar='<DISKSIZE>', help='Extra disksize, default in GB')
@utils.arg('--mem', metavar='<SERVER_MEMORY_SIZE>', help='Memory size (MB) of VM server')
@utils.arg('--keypair', metavar='<KEYPAIR>', help='ssh Keypair used for login')
@utils.arg('--disk', metavar='<DISK>', action='append', help='Virtual disks')
@utils.arg('--net', metavar='<NETWORK>', action='append', help="M|Virtual networks\n"
        "Examples:\n"
        "[random]                         random network\n"
        "[random_exit]                    random exit network\n"
        "vnet1:192.168.0.122:10:virtio    network:ipaddress:bwlimit:driver(virtio or e1000)\n")
@utils.arg('--ncpu', metavar='<SERVER_CPU_COUNT>', help='#CPU cores of VM server, default 1')
@utils.arg('--desc', metavar='<DECRIPTION>', help='Description')
@utils.arg('--allow-delete', action='store_true', help='Unlock server to allow deleting')
@utils.arg('--shutdown-behavior', metavar='<SHUTDOWN_BEHAVIOR>', choices=['stop', 'terminate'], help='Behavior after VM server shutdown, stop or terminate server')
@utils.arg('--auto-start', action='store_true', help='Auto start server after it is created')
@utils.arg('--zone', metavar='<ZONE_ID>', help='Preferred zone where virtual server should be created')
@utils.arg('--deploy', metavar='<DEPLOY_FILES>', action='append', help='Specify deploy files in virtual server file system')
@utils.arg('--group', metavar='<GROUP>', action='append', help='Group of virtual server')
@utils.arg('--tenant', metavar='<TENANT>', help='Owner tenant ID or Name')
@utils.arg('--user', metavar='<USER>', help='Owner user ID or Name')
@utils.arg('--system', action='store_true', help='Create a system VM, sysadmin ONLY option')
@utils.arg('--baremetal-host', metavar='<PREFER_HOST>', help='Prefered baremetal host')
@utils.arg('--baremetal-disk-config', metavar='<DISK_CONF>', action='append', help='Baremetal disk layout configuration')
def do_baremetal_server_create(client, args):
    """ Create a server based on baremetal """
    from yunionclient.api import glanceutils
    kwargs = {}
    kwargs['baremetal'] = True
    kwargs['name'] = args.name

    if args.flavor:
        if not args.image:
            raise Exception('Root disk image ID must be specified')
        kwargs['flavor'] = args.flavor
        kwargs['root'] = glanceutils.parse_disk_desc(client, args.image)
        if args.guest_os:
            kwargs['os'] = args.guest_os
        kwargs['extra_ext_bandwidth'] = args.extra_ext_bandwidth
        kwargs['extra_ext_disksize'] = args.extra_ext_disksize
    else:
        # if not args.mem:
        #     raise Exception('Memory size must be specified')
        if not args.disk:
            raise Exception('Disk parameters must be specified')
        if args.mem is not None:
            kwargs['vmem_size'] = args.mem
        index = 0
        for disk in args.disk:
            disk_name = 'disk.%d' % index
            index += 1
            kwargs[disk_name] = glanceutils.parse_disk_desc(client, disk)
        if args.net is not None:
            index = 0
            for net in args.net:
                net_name = 'net.%d' % index
                index += 1
                kwargs[net_name] = net
        if args.ncpu is not None:
            kwargs['vcpu_count'] = args.ncpu
    if args.keypair is not None:
        kwargs['keypair'] = args.keypair
    if args.desc is not None:
        kwargs['description'] = args.desc
    if args.allow_delete is not None and args.allow_delete:
        kwargs['disable_delete'] = False
    if args.shutdown_behavior is not None:
        kwargs['shutdown_behavior'] = args.shutdown_behavior
    if args.auto_start is not None and args.auto_start:
        kwargs['auto_start'] = True
    if args.group is not None:
        g_idx = 0
        for g in args.group:
            kwargs['group.%d' % g_idx] = g
            g_idx += 1
    if args.zone is not None:
        kwargs['prefer_zone'] = args.zone
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.user:
        kwargs['user'] = args.user
    if args.system:
        kwargs['is_system'] = True

    if args.deploy is not None:
        from . import servers
        servers.parse_deploy_info(args.deploy, kwargs)

    if args.baremetal_host:
        kwargs['prefer_baremetal'] = args.baremetal_host
    if args.baremetal_disk_config:
        index = 0
        for conf in args.baremetal_disk_config:
            conf_name = 'baremetal_disk_config.%d' % index
            index += 1
            kwargs[conf_name] = conf

    guest = client.guests.create(**kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<ID>', help='ID or Name of baremetal')
@utils.arg('--mac', metavar='<MAC>', help='MAC of baremetal NIC')
def do_baremetal_add_dns_records(client, args):
    """ Add dns record of a baremetal NIC """
    kwargs = {}
    if args.mac:
        kwargs['mac'] = args.mac
    kwargs['is_add'] = True
    bm = client.baremetals.perform_action(args.id, 'dns-update', **kwargs)
    utils.print_dict(bm)


@utils.arg('id', metavar='<ID>', help='ID or Name of baremetal')
@utils.arg('--mac', metavar='<MAC>', help='MAC of baremetal NIC')
def do_baremetal_remove_dns_records(client, args):
    """ Remove dns record of a baremetal NIC """
    kwargs = {}
    if args.mac:
        kwargs['mac'] = args.mac
    kwargs['is_add'] = False
    bm = client.baremetals.perform_action(args.id, 'dns-update', **kwargs)
    utils.print_dict(bm)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
def do_baremetal_ipmi(client, args):
    """ Get baremetal vnc info """
    info = client.baremetals.get_specific(args.id, 'ipmi')
    utils.print_dict(info)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
def do_baremetal_syncstatus(client, args):
    """ Sync baremetal status """
    info = client.baremetals.perform_action(args.id, 'syncstatus')
    utils.print_dict(info)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
def do_baremetal_sync(client, args):
    """ Sync baremetal config """
    info = client.baremetals.perform_action(args.id, 'sync-config')
    utils.print_dict(info)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
@utils.arg('ipaddr', metavar='<IPADDRESS>', help='IPMI address of baremetal')
def do_baremetal_change_ipmi_address(client, args):
    """ Change baremetal IPMI address """
    info = client.baremetals.perform_action(args.id, 'change-ipmiinfo',
                                                ip_addr=args.ipaddr)
    utils.print_dict(info)


# @utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
# @utils.arg('passwd', metavar='<PASSWORD>', help='IPMI password of baremetal')
# def do_baremetal_change_ipmi_password(client, args):
#     """ Change baremetal IPMI address """
#     info = client.baremetals.perform_action(args.id, 'change-ipmiinfo',
#                                                password=args.passwd)
#     utils.print_dict(info)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
def do_baremetal_prepare(client, args):
    """ Refresh baremetal configuration information """
    info = client.baremetals.perform_action(args.id, 'prepare')
    utils.print_dict(info)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
@utils.arg('agent', metavar='<AGENT>', help='ID of baremetal agent')
@utils.arg('--name', metavar='<VM_NAME>', help='Name of fake guest OS')
def do_baremetal_initialize(client, args):
    """ Refresh baremetal configuration information """
    kwargs = {}
    kwargs['agent'] = args.agent
    if args.name:
        kwargs['name'] = args.name
    info = client.baremetals.perform_action(args.id, 'initialize', **kwargs)
    utils.print_dict(info)


@utils.arg('id', metavar='<BAREMETAL>', help='ID of baremetal')
def do_baremetal_bmc_reset(client, args):
    """ Reset baremetal BMC """
    info = client.baremetals.perform_action(args.id, 'bmc-reset')
    utils.print_dict(info)
