from yunionclient.common import utils
from yunionclient.api import glanceutils

@utils.arg('--mem', metavar='<SERVER_MEMORY_SIZE>', help='Memory size (MB) of VM server')
@utils.arg('--ncpu', metavar='<SERVER_CPU_COUNT>', help='#CPU cores of VM server, default 1')
@utils.arg('--disk', metavar='<DISK>', action='append', help='Virtual disks (MB)')
@utils.arg('--net', metavar='<NETWORK>', action='append', help='M|Virtual networks'
        "Examples:\n"
        "[random]                         random network\n"
        "[random_exit]                    random exit network\n"
        "vnet1:192.168.0.122:10:virtio    network:ipaddress:bwlimit:driver(virtio or e1000)\n")
@utils.arg('--group', metavar='<GROUP>', action='append', help='Group of virtual server')
@utils.arg('--zone', metavar='<ZONE_ID>', help='Preferred zone where virtual server should be created')
@utils.arg('--cluster', metavar='<CLUSTER_ID>', help='Preferred cluster where virtual server should be created')
@utils.arg('--host', metavar='<HOST_ID>', help='Preferred host where virtual server should be created')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant name or ID that creates the server')
@utils.arg('--flavor', metavar='<FLAVOR>', help='Flavor ID or name')
@utils.arg('--image', metavar='<IMAGE>', help='Image ID or name')
@utils.arg('--guest-os', metavar='<OS>', choices=['windows', 'linux'], help='Guest OS type')
@utils.arg('--cpu-bound', action='store_true', help='CPU-bound type application')
@utils.arg('--io-bound', action='store_true', help='IO-bound type application')
@utils.arg('--baremetal', action='store_true', help='Create baremetal')
@utils.arg('--baremetal-disk-config', metavar='<DISK_CONFIG>', help='Baremetal disk configuration, can be raid5, raid10, softraid5, softraid10, lvm')
@utils.arg('--kvm', action='store_true', help='Guest can run KVM')
@utils.arg('--ssd', action='store_true', help='Guest run on SSD')
@utils.arg('--aggregate', metavar='<KEY:VALUE>', action='append', help='Schedule policy, key = aggregate name, value = require|exclude|prefer|avoid')
def do_scheduler_test(client, args):
    """ Emulate scheduler """
    kwargs = {}
    kwargs['suggestion'] = True
    if args.flavor and args.image:
        kwargs['flavor'] = args.flavor
        kwargs['root'] = glanceutils.parse_disk_desc(client, args.image)
        if args.guest_os:
            kwargs['os'] = args.guest_os
    elif args.mem and args.disk:
        kwargs['vmem_size'] = args.mem
        if args.ncpu:
            kwargs['vcpu_count'] = int(args.ncpu)
        disk_idx = 0
        for d in args.disk:
            kwargs['disk.%d' % disk_idx] = glanceutils \
                                                    .parse_disk_desc(client, d)
            disk_idx += 1
        if args.net:
            net_idx = 0
            for n in args.net:
                kwargs['net.%d' % net_idx] = n
                net_idx += 1
    else:
        raise Exception('Please specify either memory, disk or falvor, image')
    if args.group:
        group_idx = 0
        for g in args.group:
            kwargs['group.%d' % group_idx] = g
            group_idx += 1
    if args.host:
        kwargs['prefer_host'] = args.host
    else:
        if args.aggregate:
            index = 0
            for aggregate in args.aggregate:
                if len(aggregate.split(':')) == 2:
                    kwargs['aggregate.%d' % index] = aggregate
                    index += 1
                else:
                    print('Aggregate format error: %s' % aggregate)
                    return
        if args.cluster:
            kwargs['prefer_cluster'] = args.cluster
        elif args.zone:
            kwargs['prefer_zone'] = args.zone
    if args.tenant:
        kwargs['tenant'] = args.tenant
    kwargs['cpu_bound'] = args.cpu_bound
    kwargs['io_bound'] = args.io_bound
    if args.baremetal:
        kwargs['baremetal'] = True
        if args.baremetal_disk_config:
            kwargs['baremetal_disk_config'] = args.baremetal_disk_config
    mdict = kwargs['__meta__'] = {}
    if args.kvm is not None and args.kvm:
        mdict['kvm'] = 'enabled'
    else:
        mdict['kvm'] = 'disabled'
    if args.ssd is not None and args.ssd:
        mdict['storage_type'] = 'ssd'
    else:
        mdict['storage_type'] = 'rotational'
    result = client.scheduler.schedule(**kwargs)
    utils.print_list(result)
