import json
import os.path

from yunionclient.common import utils

from yunionclient.api import glanceutils


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--meta', action='store_true', help='Piggyback metadata')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--admin', action='store_true', help='Is admin call?')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant ID or Name')
@utils.arg('--user', metavar='<USER>', help='User ID or Name')
@utils.arg('--system', action='store_true', help='Show system objects?')
@utils.arg('--host', metavar='<HOST>', help='Show servers on the hosts')
@utils.arg('--cluster', metavar='<CLUSTER>', help='Show servers in the cluster')
@utils.arg('--zone', metavar='<ZONE>', help='Show servers in the zone')
@utils.arg('--baremetal', action='store_true', help='Show baremetal servers')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_server_list(client, args):
    """ List VM servers """
    page_info = utils.get_paging_info(args)
    if args.baremetal:
        page_info['baremetal'] = True
    if args.host:
        page_info['host'] = args.host
    elif args.cluster:
        page_info['cluster'] = args.cluster
    elif args.zone:
        page_info['zone'] = args.zone
    guests = client.guests.list(**page_info)
    utils.print_list(guests, client.guests.columns)


def parse_deploy_info(deploys, kwargs):
    index = 0
    for deploy in deploys:
        colon_pos = deploy.find(':')
        if colon_pos > 0:
            fn = deploy[:colon_pos]
            if fn[-1] == '+':
                fn = fn[:-1]
                action = 'append'
            else:
                action = 'create'
            ct = deploy[(colon_pos + 1):]
            if os.path.isfile(ct):
                with open(ct) as f:
                    ct = f.read()
            kwargs['deploy.%d.path' % index] = fn
            kwargs['deploy.%d.action' % index] = action
            kwargs['deploy.%d.content' % index] = ct
            index += 1
        else:
            raise Exception("Malformed deploy string")

@utils.arg('name', metavar='<SERVER_NAME>', help='Name of VM server')
@utils.arg('--flavor', metavar='<FLAVOR_ID>', help='ID of server flavor')
@utils.arg('--image', metavar='<ROOT_IMAGE_ID>', help='ID of root disk image')
@utils.arg('--guest-os', metavar='<OS>', choices=['windows', 'linux'], help='Guest OS type')
@utils.arg('--extra-ext-bandwidth', metavar='<BANDWIDTH>', help='Extra external bandwidth, default in Mbps')
@utils.arg('--extra-ext-disksize', metavar='<DISKSIZE>', help='Extra disksize, default in GB')
@utils.arg('--snapshot', metavar='<SNAPSHOT>', help='Snapshot from which the server is created')
@utils.arg('--snapshot-disk', metavar='<SNAPSHOT>', help='Snapshot disk used as a data disk')
@utils.arg('--mem', metavar='<SERVER_MEMORY_SIZE>', help='Memory size (MB) of VM server')
@utils.arg('--keypair', metavar='<KEYPAIR>', help='ssh Keypair used for login')
@utils.arg('--disk', metavar='<DISK>', action='append', help='Virtual disks')
@utils.arg('--net', metavar='<NETWORK>', action='append', help="M|Virtual networks\n"
        "Examples:\n"
        "[random]                         random network\n"
        "[random_exit]                    random exit network\n"
        "vnet1:192.168.0.122:10:virtio    network:ipaddress:bwlimit:driver(virtio or e1000)\n")
@utils.arg('--cdrom', metavar='<IMAGE_ID>', help='ISO image ID')
@utils.arg('--ncpu', metavar='<SERVER_CPU_COUNT>', help='#CPU cores of VM server, default 1')
@utils.arg('--vga', metavar='<VGA>', choices=['std', 'vmware', 'cirrus', 'qxl'], help='VGA driver')
@utils.arg('--vdi', metavar='<VDI>', choices=['vnc', 'spice'], help='VDI protocool')
@utils.arg('--bios', metavar='<BIOS>', choices=['BIOS', 'UEFI'], help='BIOS')
@utils.arg('--desc', metavar='<DECRIPTION>', help='Description')
@utils.arg('--boot', metavar='<BOOT_DEVICE>', choices=['disk', 'cdrom'], help='Boot device')
@utils.arg('--allow-delete', action='store_true', help='Unlock server to allow deleting')
@utils.arg('--shutdown-behavior', metavar='<SHUTDOWN_BEHAVIOR>', choices=['stop', 'terminate'], help='Behavior after VM server shutdown, stop or terminate server')
@utils.arg('--auto-start', action='store_true', help='Auto start server after it is created')
@utils.arg('--zone', metavar='<ZONE_ID>', help='Preferred zone where virtual server should be created')
@utils.arg('--host', metavar='<HOST_ID>', help='Preferred host where virtual server should be created')
@utils.arg('--cluster', metavar='<CLUSTER>', help='Preferred cluster where virtual server should be created')
@utils.arg('--deploy', metavar='<DEPLOY_FILES>', action='append', help='Specify deploy files in virtual server file system')
@utils.arg('--group', metavar='<GROUP>', action='append', help='Group of virtual server')
@utils.arg('--tenant', metavar='<TENANT>', help='Owner tenant ID or Name')
@utils.arg('--user', metavar='<USER>', help='Owner user ID or Name')
@utils.arg('--system', action='store_true', help='Create a system VM, sysadmin ONLY option')
@utils.arg('--cpu-bound', action='store_true', help='CPU-bound type application')
@utils.arg('--io-bound', action='store_true', help='IO-bound type application')
@utils.arg('--kvm', action='store_true', help='Guest can run KVM')
@utils.arg('--ssd', action='store_true', help='Guest can run on SSD')
@utils.arg('--billing-type', metavar='<BILLING_TYPE>', choices=['contract', 'postpay'], help='Billing type for guest')
@utils.arg('--io-hardlimit', action='store_true', help='IO-hardlimit type application')
@utils.arg('--user-data', metavar='<USERDATAFILEPATH>', help='User data file path, e.g. ~/cloud-config.yaml')
@utils.arg('--aggregate', metavar='<KEY:VALUE>', action='append', help='Schedule policy, key = aggregate name, value = require|exclude|prefer|avoid')
@utils.arg('--secgroup', metavar='<SECGROUP>', help='Secgroup ID or Name')
@utils.arg('--container', action='store_true', help='Container Server')
@utils.arg('--set-conf', metavar='<CONTAINERSETCONFPATH>', help='Container set config file path')
@utils.arg('--hypervisor', metavar='<HYPERVISOR>', default='kvm', choices=['kvm', 'esxi', 'baremetal'], help='Server hypervisor type')
def do_server_create(client, args):
    """ Create a VM server """
    kwargs = {}
    kwargs['name'] = args.name
    if args.snapshot:
        kwargs['snapshot'] = args.snapshot
    elif args.container:
        kwargs['container'] = True
        if args.set_conf is not None:
            with open(args.set_conf) as set_conf:
                kwargs['container_set'] = json.load(set_conf)
        elif args.image is not None:
            kwargs['container_set'] = {'containers': [{'image': args.image}]}
            if not args.mem:
                raise Exception('Memory size must be specified')
            kwargs['container_set']['containers'][0].update({'mem': args.mem})
            if args.ncpu is not None:
                kwargs['container_set']['containers'][0].update({'cpu': args.ncpu})
        else:
            raise Exception('Image or set_conf must be specified')
        if args.net is not None:
            index = 0
            for net in args.net:
                net_name = 'net.%d' % index
                index += 1
                kwargs[net_name] = net
    else:
        if args.snapshot_disk:
            kwargs['snapshot'] = args.snapshot_disk
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
            if not args.mem:
                raise Exception('Memory size must be specified')
            if not args.disk:
                raise Exception('Disk parameters must be specified')
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
        if args.cdrom is not None:
            img = client.images.get(args.cdrom)
            kwargs['cdrom'] = img.id
        if args.vga is not None:
            kwargs['vga'] = args.vga
        if args.vdi is not None:
            kwargs['vdi'] = args.vdi
        if args.bios is not None:
            kwargs['bios'] = args.bios
        if args.deploy is not None:
            parse_deploy_info(args.deploy, kwargs)
        if args.boot is not None:
            if args.boot == 'disk':
                kwargs['boot_order'] = 'cdn'
            else:
                kwargs['boot_order'] = 'dcn'
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
    if args.host:
        kwargs['prefer_host'] = args.host
    else:
        if args.cluster:
            kwargs['prefer_cluster'] = args.cluster
        elif args.zone:
            kwargs['prefer_zone'] = args.zone
        if args.aggregate:
            index = 0
            for aggregate in args.aggregate:
                if len(aggregate.split(':')) == 2:
                    kwargs['aggregate.%d' % index] = aggregate
                    index += 1
                else:
                    print('Aggregate format error: %s' % aggregate)
                    return
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.user:
        kwargs['user'] = args.user
    if args.system:
        kwargs['is_system'] = True
    if args.billing_type:
        kwargs['billing_type'] = args.billing_type

    mdict = kwargs['__meta__'] = {}
    if args.kvm is not None and args.kvm:
        mdict['kvm'] = 'enabled'
    else:
        mdict['kvm'] = 'disabled'
    if args.ssd is not None and args.ssd:
        mdict['storage_type'] = 'ssd'
    else:
        mdict['storage_type'] = 'rotational'
    if args.cpu_bound:
        kwargs['cpu_bound'] = args.cpu_bound
    if args.io_bound:
        kwargs['io_bound'] = args.io_bound
    if args.io_hardlimit:
        kwargs['io_hardlimit'] = args.io_hardlimit

    if args.secgroup:
        kwargs['secgroup'] = args.secgroup

    if args.user_data:
        if not os.path.exists(args.user_data):
            print('User data file:%s not found' % args.user_data)
            return
        if os.path.getsize(args.user_data) > 16*1024:
            print('User data is limited to 16 KB. ')
            return

        import base64
        with open(args.user_data) as f:
            kwargs['user_data'] = base64.b64encode(f.read())

    if args.hypervisor:
        kwargs['hypervisor'] = args.hypervisor

    guest = client.guests.create(**kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of VM server to update')
@utils.arg('--name', metavar='<SERVER_NAME>', help='Name of VM server')
@utils.arg('--mem', metavar='<SERVER_MEMORY_SIZE>', help='Memory size (MB) of VM server')
@utils.arg('--ncpu', metavar='<SERVER_CPU_COUNT>', help='#CPU cores of VM server, default 1')
@utils.arg('--vga', metavar='<VGA>', choices=['std', 'vmware', 'cirrus', 'qxl'], help='VGA driver')
@utils.arg('--vdi', metavar='<VDI>', choices=['vnc', 'spice'], help='VDI protocol')
@utils.arg('--bios', metavar='<BIOS>', choices=['BIOS', 'UEFI'], help='BIOS')
@utils.arg('--desc', metavar='<DECRIPTION>', help='Description')
@utils.arg('--boot', metavar='<BOOT_DEVICE>', choices=['disk', 'cdrom'], help='Boot device')
@utils.arg('--delete', metavar='<ALLOW_DELETE>', choices=['enable', 'disable'], help='Lock server to prevent from deleting')
@utils.arg('--shutdown-behavior', metavar='<SHUTDOWN_BEHAVIOR>', choices=['stop', 'terminate'], help='Behavior after VM server shutdown, stop or terminate server')
def do_server_update(client, args):
    """
    Update property of a VM server
    Some changes require VM server restart to take effect
    """
    kwargs = {}
    if args.name is not None:
        kwargs['name'] = args.name
    if args.mem is not None:
        kwargs['vmem_size'] = args.mem
    if args.ncpu is not None:
        kwargs['vcpu_count'] = args.ncpu
    if args.vga is not None:
        kwargs['vga'] = args.vga
    if args.vdi is not None:
        kwargs['vdi'] = args.vdi
    if args.bios is not None:
        kwargs['bios'] = args.bios
    if args.desc is not None:
        kwargs['description'] = args.desc
    if args.boot is not None:
        if args.boot == 'disk':
            kwargs['boot_order'] = 'cdn'
        else:
            kwargs['boot_order'] = 'dcn'
    if args.delete is not None:
        if args.delete == 'disable':
            kwargs['disable_delete'] = True
        else:
            kwargs['disable_delete'] = False
    if args.shutdown_behavior is not None:
        kwargs['shutdown_behavior'] = args.shutdown_behavior
    if len(kwargs) == 0:
        raise Exception("No data to update")
    guest = client.guests.update(args.id, **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to delete')
def do_server_delete(client, args):
    """ Delete a virtual server """
    guest = client.guests.delete(args.id)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to purge')
def do_server_purge(client, args):
    """ Purge a virtual server on a dead host """
    guest = client.guests.perform_action(args.id, 'purge')
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to migrate')
@utils.arg('--host', metavar='<HOST_ID>', help='Preferred host where virtual server should migrate to')
@utils.arg('--copy', action='store_true', help='Do not use live migration, hard copy migration')
def do_server_migrate(client, args):
    """ Delete a virtual server """
    kwargs = {}
    if args.host is not None:
        kwargs['prefer_host'] = args.host
    if args.copy:
        action = 'migrate'
    else:
        action = 'live-migrate'
    guest = client.guests.perform_action(args.id, action, **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to start')
@utils.arg('--qemu-version', metavar='<QEMU_VERSION>', help='Suggest a qemu version')
def do_server_start(client, args):
    """ Start a virtual server """
    kwargs = {}
    if args.qemu_version:
        kwargs['qemu_version'] = args.qemu_version
    guest = client.guests.perform_action(args.id, 'start', **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual VM server to shutdown')
@utils.arg('--force', action='store_true', help='Shutdown VM server by force')
def do_server_stop(client, args):
    """ Stop a virtual server """
    if args.force is not None and args.force:
        is_force = True
    else:
        is_force = False
    guest = client.guests.perform_action(args.id, 'stop', is_force=is_force)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual VM server to suspend')
def do_server_suspend(client, args):
    """ Suspend a virtual server """
    guest = client.guests.perform_action(args.id, 'suspend')
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual VM server to resume')
def do_server_resume(client, args):
    """ resume a virtual server """
    guest = client.guests.perform_action(args.id, 'resume')
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to reset')
@utils.arg('--hard', action='store_true', help='Hard reset')
def do_server_reset(client, args):
    """ Stop a virtual server """
    if args.hard is not None and args.hard:
        is_hard = True
    else:
        is_hard = False
    guest = client.guests.perform_action(args.id, 'reset', is_hard=is_hard)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to reset')
@utils.arg('--keypair', metavar='<KEYPAIR>', help='ssh Keypair used for login')
@utils.arg('--delete-keypair', action='store_true', help='Remove ssh Keypairs')
@utils.arg('--deploy', metavar='<DEPLOY_FILES>', action='append', help='Specify deploy files in virtual server file system')
@utils.arg('--reset-password', action='store_true', help='Force reset password')
def do_server_deploy(client, args):
    """ Deploy hostname and keypair to a stopped virtual server """
    kwargs = {}
    if args.delete_keypair:
        kwargs['__delete_keypair__'] = True
    elif args.keypair:
        kwargs['keypair'] = args.keypair
    if args.deploy:
        parse_deploy_info(args.deploy, kwargs)
    if args.reset_password:
        kwargs['reset_password'] = True
    guest = client.guests.perform_action(args.id, 'deploy', **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to get vnc info')
def do_server_vnc(client, args):
    """ Show VNC info of a virtual server """
    guest = client.guests.get_specific(args.id, 'vnc')
    utils.print_dict(guest)

@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to get ip info')
def do_server_ips(client, args):
    """ Show IP info of a virtual server """
    guest = client.guests.get_specific(args.id, 'ips')
    guest['ips'] = ', '.join(guest.get('ips', []))
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to get metadata info')
@utils.arg('--field', metavar='<METADATA_FIELD>', help='Field name of metadata')
def do_server_metadata(client, args):
    """ Show metadata info of a virtual server """
    kwargs = {}
    if args.field is not None:
        kwargs['field'] = args.field
    guest = client.guests.get_metadata(args.id, **kwargs)
    if isinstance(guest, dict):
        utils.print_dict(guest)
    else:
        print(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to set metadata info')
@utils.arg('--tags', metavar='<TAGS>', action='append', help='Tags info')
def do_server_set_tag(client, args):
    """ Set metadata info of a virtual server """
    kwargs = {}
    for tag in args.tags:
        info = tag.split('=')
        if len(info) == 2:
            kwargs[info[0]] = info[1]
        elif len(info) == 1:
            kwargs[info[0]] = ''
        else:
            raise Exception('Invalid tag info %s', tag)
    guest = client.guests.perform_action(args.id, 'set-user-metadata', **kwargs)
    if isinstance(guest, dict):
        utils.print_dict(guest)
    else:
        print(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to set metadata info')
@utils.arg('--tags', metavar='<TAGS>', action='append', help='Tags info')
def do_server_add_tag(client, args):
    """ Add metadata info of a virtual server """
    kwargs = {}
    for tag in args.tags:
        info = tag.split('=')
        if len(info) == 2:
            kwargs[info[0]] = info[1]
        elif len(info) == 1:
            kwargs[info[0]] = ''
        else:
            raise Exception('Invalid tag info %s', tag)
    guest = client.guests.perform_action(args.id, 'user-metadata', **kwargs)
    if isinstance(guest, dict):
        utils.print_dict(guest)
    else:
        print(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to get password')
@utils.arg('--key', metavar='<PRIVATE_KEY>', help='Path to private key of specific keypair')
def do_server_password(client, args):
    """ Get Password of a virtual server """
    secret = client.guests.get_metadata(args.id, field='login_key')
    if secret is not None:
        if args.key is None:
            guest = client.guests.get(args.id)
            if isinstance(guest, dict):
                idstr = guest['id']
            else:
                idstr = guest.id
            print(utils.decrypt_aes_base64(idstr, secret))
        elif os.path.exists(args.key):
            with open(args.key) as f:
                privkey = f.read()
                print(utils.decrypt_base64(privkey, secret))
        else:
            raise Exception('Key file not found')
    else:
        raise Exception('No login password')


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to get server status')
def do_server_status(client, args):
    """ Shortcut to get server status of a virtual server """
    guest = client.guests.get_specific(args.id, 'status')
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to sync')
def do_server_sync(client, args):
    """ Sync configuration with a virtual server """
    guest = client.guests.perform_action(args.id, 'sync')
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to sync status')
def do_server_syncstatus(client, args):
    """ Force synchronize status of a virtual server across controller and host"""
    guest = client.guests.perform_action(args.id, 'syncstatus')
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to get monitor info')
@utils.arg('--cmd', metavar='<COMMAND>', required=True, help='ID of virtual server to get monitor info')
def do_server_monitor(client, args):
    """ Show monitor info of a virtual server """
    guest = client.guests.get_specific(args.id, 'monitor', command=args.cmd)
    print(guest['results'])


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to get monitor info')
@utils.arg('--keys', metavar='<KEYS>', required=True, help='Special keys to send, eg. ctrl, alt, f12, shift, etc, separated by "-"')
@utils.arg('--hold', metavar='<MILLISECONDS>', help='Hold key for specified milliseconds')
def do_server_send_keys(client, args):
    """ Show monitor info of a virtual server """
    guest = client.guests.perform_action(args.id, 'sendkeys', keys=args.keys, duration=args.hold)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to show')
@utils.arg('--with-meta', action='store_true', help='With meta data')
def do_server_show(client, args):
    """ Show a virtual server """
    kwargs = {}
    if args.with_meta:
        kwargs['with_meta'] = True
    guest = client.guests.get(args.id, **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER>', help='ID of virtual server, or [all] for all servers')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--admin', action='store_true', help='Is admin call?')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant ID or Name')
@utils.arg('--system', action='store_true', help='Show system objects?')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_server_network_list(client, args):
    """ List all virtual networks of a virtual server """
    page_info = utils.get_paging_info(args)
    if args.id != 'all':
        guestnetworks = client.guestnetworks.list_descendent(args.id,
                                                                **page_info)
    else:
        guestnetworks = client.guestnetworks.list(**page_info)
    utils.print_list(guestnetworks, client.guestnetworks.columns)


@utils.arg('id', metavar='<SERVER>', help='ID of virtual server')
@utils.arg('--net', metavar='<NETWORK>', required=True, help='ID of virtual network')
def do_server_network_show(client, args):
    """ Show details of virtual network interface of a virtual server """
    guestnetwork = client.guestnetworks.get(args.id, args.net)
    utils.print_dict(guestnetwork)


@utils.arg('id', metavar='<SERVER>', help='ID of virtual server')
@utils.arg('net', metavar='<NETWORK_DESC>', help='Network description')
def do_server_attach_network(client, args):
    """ Attach a virtual network to a virtual server """
    guest = client.guests.perform_action(args.id, 'attachnetwork',
                                                            net_desc=args.net)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER>', help='ID of virtual server')
@utils.arg('net', metavar='<NETWORK>', help='ID of virtual network to detach')
@utils.arg('--reserve', action='store_true', help='Put the release IP address into reserved address pool')
def do_server_detach_network(client, args):
    """ Detach the virtual network fron a virtual server """
    kwargs = {'net_id': args.net}
    if args.reserve:
        kwargs['reserve'] = True
    guest = client.guests.perform_action(args.id, 'detachnetwork', **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER>', help='ID of virtual server')
@utils.arg('--net', metavar='<NETWORK>', required=True, help='ID of virtual network')
@utils.arg('--driver', metavar='<DRIVER>', choices=['virtio', 'e1000', 'rtl8139'], help='Driver model of vNIC')
#@utils.arg('--bw-limit', metavar='<BANDWIDTH>', help='Bandwidth limit, in Mbps')
@utils.arg('--index', metavar='<INDEX>', help='Index of NIC')
@utils.arg('--ifname', metavar='<IFNAME>', help='Host interface name of NIC')
def do_server_network_update(client, args):
    """ Update details of virtual network interface of a virtual server """
    kwargs = {}
    if args.driver is not None:
        kwargs['driver'] = args.driver
    if args.index is not None:
        kwargs['index'] = args.index
    if args.ifname is not None:
        kwargs['ifname'] = args.ifname
    #if args.bw_limit:
    #    kwargs['bw_limit'] = int(args.bw_limit)
    if len(kwargs) == 0:
        raise Exception('No data to update')
    guestnetwork = client.guestnetworks.update(args.id, args.net, **kwargs)
    utils.print_dict(guestnetwork)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('index', metavar='<NIC_INDEX>', type=int, help='Index of NIC')
@utils.arg('bw', metavar='<BANDWIDTH>', type=int, help='Bandwidth in Mbps')
def do_server_change_bandwidth(client, args):
    """ Change server network bandwidth in Mbps """
    guest = client.guests.perform_action(args.id, 'change-bandwidth',
                                        index=args.index,
                                        bandwidth=args.bw)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server, or [all] for all servers')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--admin', action='store_true', help='Is admin call?')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant ID or Name')
@utils.arg('--system', action='store_true', help='Show system objects?')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_server_disk_list(client, args):
    """ List all virtual disks of a virtual server """
    page_info = utils.get_paging_info(args)
    if args.id != 'all':
        guestdisks = client.guestdisks.list_descendent(args.id, **page_info)
    else:
        guestdisks = client.guestdisks.list(**page_info)
    utils.print_list(guestdisks, client.guestdisks.columns)


@utils.arg('id', metavar='<SERVER>', help='ID of virtual server')
@utils.arg('--disk', metavar='<DISK>', required=True, help='ID of virtual disk')
def do_server_disk_show(client, args):
    """ Show details of a virtual disk of a virtual server """
    guestdisk = client.guestdisks.get(args.id, args.disk)
    utils.print_dict(guestdisk)


@utils.arg('id', metavar='<SERVER>', help='ID of virtual server')
@utils.arg('--disk', metavar='<DISK>', required=True, help='ID of virtual disk')
@utils.arg('--driver', metavar='<DRIVER>', choices=['virtio', 'ide', 'scsi'], help='Driver of vDisk')
@utils.arg('--cache', metavar='<CACHE_MODE>', choices=['writethrough', 'none', 'writeback'], help='Cache mode of vDisk')
@utils.arg('--aio', metavar='<AIO_MODE>', choices=['native', 'threads'], help='Asynchronous IO mode of vDisk')
@utils.arg('--index', metavar='<INDEX>', help='Index of vDisk')
def do_server_disk_update(client, args):
    """ Update details of a virtual disk of a virtual server """
    kwargs = {}
    if args.driver is not None:
        kwargs['driver'] = args.driver
    if args.cache is not None:
        kwargs['cache_mode'] = args.cache
    if args.aio is not None:
        kwargs['aio_mode'] = args.aio
    if args.index is not None and int(args.index) >= 0:
        kwargs['index'] = int(args.index)
    if len(kwargs) <= 0:
        raise Exception('No data to update')
    guestdisk = client.guestdisks.update(args.id, args.disk, **kwargs)
    utils.print_dict(guestdisk)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('--disk', metavar='<DISK>', required=True, action='append', help='Disk description of a virtual disk')
def do_server_create_disk(client, args):
    """ Create a disk and attach it to a virtual server """
    kwargs = {}
    index = 0
    for disk in args.disk:
        kwargs['disk.%d' % index] = glanceutils.parse_disk_desc(client, disk)
        index += 1
    guest = client.guests.perform_action(args.id, 'createdisk', **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('--disk', metavar='<DISK_ID>', required=True, help='Disk ID of an existing virtual disk')
@utils.arg('--driver', metavar='<DRIVER>', choices=['virtio', 'ide', 'scsi'], help='Driver')
@utils.arg('--cache', metavar='<CACHE_MODE>', choices=['writeback', 'none', 'writethrought'], help='Cache mode')
def do_server_attach_disk(client, args):
    """ Attach an existing virtual disks to a virtual server """
    kwargs = {}
    kwargs['disk_id'] = args.disk
    if args.driver:
        kwargs['driver'] = args.driver
    if args.cache:
        kwargs['cache'] = args.cache
    guest = client.guests.perform_action(args.id, 'attachdisk', **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('--iso', metavar='<DISK_ID>', required=True, help='Image ID of an ISO')
def do_server_insert_iso(client, args):
    """ Insert an ISO to a virtual server """
    img = client.images.get(args.iso)
    guest = client.guests.perform_action(args.id, 'insertiso',
                                                        image_id=img.id)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
def do_server_eject_iso(client, args):
    """ Eject ISO image from a virtual server """
    guest = client.guests.perform_action(args.id, 'ejectiso')
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
def do_server_iso(client, args):
    """ Show ISO image information of a virtual server """
    iso = client.guests.get_specific(args.id, 'iso')
    utils.print_dict(iso)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('--disk', metavar='<DISK_ID>', required=True, help='Disk ID or Name of an attached virtual disk')
@utils.arg('--keep', action='store_true', help='Keep disk even if the disk has flag of auto_delete when detached')
def do_server_detach_disk(client, args):
    """ Detach a disk from a virtual server """
    if args.keep is not None and args.keep:
        keep_disk = True
    else:
        keep_disk = False
    guest = client.guests.perform_action(args.id, 'detachdisk', \
                                        disk_id=args.disk, keep_disk=keep_disk)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('--tenant', metavar='<TENANT>', required=True, help='Target tenant')
@utils.arg('--user', metavar='<USER>', required=True, help='Target user')
def do_server_change_owner(client, args):
    """ Change owner of a virtual server """
    kwargs = {}
    kwargs['tenant'] = args.tenant
    kwargs['user'] = args.user
    guest = client.guests.perform_action(args.id, 'change-owner', **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('flavor', metavar='<FLAVOR>', help='Target id or name')
@utils.arg('--force', action='store_true', help='Force set server flavor')
@utils.arg('--extra-ext-bandwidth', metavar='<BANDWIDTH>', help='Extra external bandwidth, default in Mbps')
@utils.arg('--extra-ext-disksize', metavar='<DISKSIZE>', help='Extra data disksize, default in GB')
def do_server_change_flavor(client, args):
    """ Change flavor of a virtual server """
    if args.force:
        guest = client.guests.perform_action(args.id, 'force-set-flavor',
                                                        flavor=args.flavor)
    else:
        kwargs = {}
        kwargs['flavor'] = args.flavor
        kwargs['extra_ext_bandwidth'] = args.extra_ext_bandwidth
        kwargs['extra_ext_disksize'] = args.extra_ext_disksize
        guest = client.guests.perform_action(args.id, 'change-flavor', **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('--image', metavar='<IMAGE_ID>', help='Root disk template ID')
def do_server_rebuild_root(client, args):
    """ Rebuild root disk of a virtual server """
    kwargs = {}
    if args.image:
        img = client.images.get(args.image)
        kwargs['image_id'] = img.id
    guest = client.guests.perform_action(args.id, 'rebuild-root', **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('proto', metavar='<PROTOCOL>', choices=['gw', 'icmp', 'tcp', 'udp', 'http', 'https'], help='Network protocal of server service')
@utils.arg('-port', metavar='<PORT>', type=int, help='Transport protocol service port')
def do_server_add_network_service(client, args):
    """ Add network role to a system VM """
    kwargs = {}
    kwargs['proto'] = args.proto
    if args.port and args.port > 0:
        kwargs['port'] = args.port
    roles = client.guests.perform_action(args.id, 'add-network-service',
                                                        **kwargs)
    print(roles)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('proto', metavar='<PROTOCOL>', choices=['gw', 'icmp', 'tcp', 'udp', 'http', 'https'], help='Network protocal of server service')
@utils.arg('-port', metavar='<PORT>', type=int, help='Transport protocol service port')
def do_server_remove_network_service(client, args):
    """ Remove network role from a system VM """
    kwargs = {}
    kwargs['proto'] = args.proto
    if args.port and args.port > 0:
        kwargs['port'] = args.port
    roles = client.guests.perform_action(args.id, 'remove-network-service',
                                                            **kwargs)
    print(roles)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('secgrp', metavar='<SECURITY_GROUP>', help='ID of Security Group')
def do_server_assign_secgroup(client, args):
    """ Assign security group to a VM """
    guest = client.guests.perform_action(args.id, 'assign-secgroup',
                                                secgrp=args.secgrp)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
def do_server_revoke_secgroup(client, args):
    """ Revoke security group from a VM """
    guest = client.guests.perform_action(args.id, 'assign-secgroup')
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('secgrp', metavar='<SECURITY_GROUP>', help='ID of Security Group')
def do_server_assign_admin_secgroup(client, args):
    """ Assign administrative security group to a VM """
    guest = client.guests.perform_action(args.id, 'assign-admin-secgroup',
                                                secgrp=args.secgrp)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
def do_server_revoke_admin_secgroup(client, args):
    """ Revoke administrative security group to a VM """
    guest = client.guests.perform_action(args.id, 'assign-admin-secgroup')
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('--timestamp', metavar='<TIMESTAMP>', help='Timestamp')
def do_server_restore_snapshot(client, args):
    """ Restore snapshot """
    kwargs = {}
    if args.timestamp:
        kwargs['timestamp'] = args.timestamp
    guest = client.guests.perform_action(args.id, 'restore-snapshot',
                                                **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('--net', metavar='<NETWORK_ID>', help='Specify network')
def do_server_add_dns_records(client, args):
    """ Manually add dns record of a server to DNS server """
    kwargs = {}
    kwargs['is_add'] = True
    if args.net:
        kwargs['network'] = args.net
    guest = client.guests.perform_action(args.id, 'dns-update',
                                                **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('--net', metavar='<NETWORK_ID>', help='Specify network')
def do_server_remove_dns_records(client, args):
    """ Manually remove dns records of a server from DNS server """
    kwargs = {}
    kwargs['is_add'] = False
    if args.net:
        kwargs['network'] = args.net
    guest = client.guests.perform_action(args.id, 'dns-update',
                                                **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('tags', metavar='<APPTAGS>', help='App tags like cpu_bound/io_bound, seprated by comma')
def do_server_set_apptags(client, args):
    """ Set Application Tags like cpu_bound/io_bound used in scheduler """
    kwargs = {}
    kwargs['tags'] = args.tags
    guest = client.guests.perform_action(args.id, 'set_apptags', **kwargs)

    utils.print_dict(guest)

@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('file', metavar='<USERDATAFILEPATH>', help='User data file path, e.g. ~/cloud-config.yaml')
def do_server_set_user_data(client, args):
    """ Set User Data """
    if not os.path.exists(args.file):
        print('user data file:%s not found' % args.file)
        return
    if os.path.getsize(args.file) > 16*1024:
        print('User data is limited to 16 KB. ')
        return

    import base64
    with open(args.file) as f:
        kwargs = {'user_data': base64.b64encode(f.read())}

    guest = client.guests.perform_action(args.id, 'set_user_data', **kwargs)
    utils.print_dict(guest)

@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to get metadata info')
def do_server_extra_options(client, args):
    """ Show extra options in QEMU start script """
    options = client.guests.get_metadata(args.id, field='extra_options')
    utils.print_dict(json.loads(options))


@utils.arg('id', metavar='<SERVER_ID>', help='Id of virtual server to get extra options')
@utils.arg('key', metavar='<KEY>', help='Option key')
@utils.arg('value', metavar='<VALUE>', help='Option value')
def do_server_add_extra_option(client, args):
    """
    Set extra options in QEMU start script
    Changes require VM server restart to take effect
    """
    kwargs = {}
    kwargs['key'] = args.key
    kwargs['value'] = args.value
    guest = client.guests.perform_action(args.id, 'set_extra_option', **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='Id of virtual server to get extra options')
@utils.arg('key', metavar='<KEY>', help='Option key')
def do_server_remove_extra_option(client, args):
    """
    Del extra options in QEMU start script
    Changes require VM server restart to take effect
    """
    kwargs = {}
    kwargs['key'] = args.key
    guest = client.guests.perform_action(args.id, 'del_extra_option', **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('name', metavar='<IMAGE_NAME>', help='Image name')
@utils.arg('--public', action='store_true', help='the saved image publicly available')
@utils.arg('--use-id', metavar='<USE_IMAGE_ID>', help='Saved image use specified ID')
@utils.arg('--notes', metavar='<NOTES>', help='Notes')
def do_server_save_image(client, args):
    """ Save root disk to new image and upload to glance. """
    kwargs = {}
    kwargs['name'] = args.name
    if args.public is not None and args.public:
        kwargs['is_public'] = True
    else:
        kwargs['is_public'] = False
    if args.use_id:
        img = client.images.get(args.use_id)
        kwargs['use_id'] = img.id
    if args.notes:
        kwargs['notes'] = args.notes
    guest = client.guests.perform_action(args.id, 'save_image', **kwargs)
    utils.print_dict(guest)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to get firewall rules')
def do_server_firewall_rules(client, args):
    """ Show firewall rules of a virtual server """
    info = client.guests.get_specific(args.id, 'firewall-rules')
    utils.print_dict(info)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server to get firewall rules')
def do_server_remove_statefile(client, args):
    """ Remove statefile of a suspend server """
    info = client.guests.perform_action(args.id, 'remove-statefile')
    utils.print_dict(info)


@utils.arg('id', metavar='<SERVER_ID>', help='ID of virtual server')
@utils.arg('throughput', metavar='<MAX_THROUGHPUT_MBPS>', help='Maximal throughput in MBytes/seconds')
@utils.arg('iops', metavar='<MAX_IOPS>', help='Maximal iops')
def do_server_io_throttle(client, args):
    """ Do io throttle for a virtual server """
    guest = client.guests.perform_action(args.id, 'io-throttle',
                                            throughput=args.throughput,
                                            iops=args.iops)
    utils.print_dict(guest)
