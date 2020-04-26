import yunionclient

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
@utils.arg('--unused', action='store_true', help='Show unused disks')
@utils.arg('--field', metavar='<FIELD>', action='append', help='Show only specified fields')
def do_disk_list(client, args):
    """ List all virtual disk """
    page_info = utils.get_paging_info(args)
    unused = getattr(args, 'unused', None)
    if unused:
        page_info['unused'] = True
    disks = client.disks.list(**page_info)
    utils.print_list(disks, client.disks.columns)


@utils.arg('id', metavar='<STORAGE_ID>', help='Name of storage to use')
@utils.arg('--disk', metavar='<DISK_INFO>', required=True, help='Image id or Size of virtual disk in MB, optionally specify file system')
@utils.arg('--name', metavar='<DISK_NAME>', required=True, help='Name of virtual disk to create')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
def do_storage_create_disk(client, args):
    """ Create a virtual disk """
    kwargs = {}
    kwargs['name'] = args.name
    kwargs['disk'] = glanceutils.parse_disk_desc(client, args.disk)
    #kwargs['storage_id'] = args.storage_id
    if args.desc is not None:
        kwargs['description'] = args.desc
    disk = client.storages.create_descendent(args.id,
                    yunionclient.api.disks.DiskManager, **kwargs)
    utils.print_dict(disk)


@utils.arg('id', metavar='<DISK_ID>', help='ID of virtual disk to delete')
def do_disk_delete(client, args):
    """ Delete a virtual disk """
    disk = client.disks.delete(args.id)
    utils.print_dict(disk)


@utils.arg('id', metavar='<DISK_ID>', help='ID of virtual disk to purge')
def do_disk_purge(client, args):
    """ Force delete a virtual disk even if it is on a disabled host """
    disk = client.disks.perform_action(args.id, 'purge')
    utils.print_dict(disk)


@utils.arg('id', metavar='<DISK_ID>', help='ID of virtual disk to delete')
@utils.arg('--auto-delete', metavar='<BOOLEAN>', choices=['enable', 'disable'], help='enable/disable auto delete of disk')
@utils.arg('--name', metavar='<NAME>', help='Name of virtual disk')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description of a virtual disk')
def do_disk_update(client, args):
    """ Update property of a virtual disk """
    kwargs = {}
    if args.auto_delete is not None:
        if args.auto_delete == 'enable':
            kwargs['auto_delete'] = True
        else:
            kwargs['auto_delete'] = False
    if args.name is not None:
        kwargs['name'] = args.name
    if args.desc is not None:
        kwargs['description'] = args.desc
    if len(kwargs) == 0:
        raise Exception("No data to update")
    disk = client.disks.update(args.id, **kwargs)
    utils.print_dict(disk)


@utils.arg('id', metavar='<DISK_ID>', help='ID of virtual disk to make public')
def do_disk_public(client, args):
    """ Make a virtual disk publicly available """
    disk = client.disks.perform_action(args.id, 'public')
    utils.print_dict(disk)


@utils.arg('id', metavar='<DISK_ID>', help='ID of virtual disk to make private')
def do_disk_private(client, args):
    """ Make a virtual disk for private use only """
    disk = client.disks.perform_action(args.id, 'private')
    utils.print_dict(disk)


@utils.arg('id', metavar='<DISK_ID>', help='ID of virtual disk to save')
@utils.arg('--name', metavar='<IMAGE_NAME>', required=True, help='Name of saved image')
@utils.arg('--public', action='store_true', help='the saved image publicly available')
@utils.arg('--use-id', metavar='<USE_IMAGE_ID>', help='Saved image use specified ID')
def do_disk_save(client, args):
    """ Save a virtual disk to image server (Glance) """
    if args.public is not None and args.public:
        is_public = True
    else:
        is_public = False
    use_id = None
    if args.use_id:
        img = client.images.get(args.use_id)
        use_id = img.id
    disk = client.disks.perform_action(args.id, 'save', name=args.name,
                                                is_public=is_public,
                                                use_id=use_id)
    utils.print_dict(disk)


@utils.arg('id', metavar='<DISK_ID>', help='ID of virtual disk to save')
@utils.arg('size', metavar='<SIZE>', help='New size of disk (MB)')
def do_disk_resize(client, args):
    """ Resize an offline virtual disk (not attached to running server) """
    disk = client.disks.perform_action(args.id, 'resize',
                                    size=args.size)
    utils.print_dict(disk)


@utils.arg('id', metavar='<DISK_ID>', help='ID of virtual disk to save')
@utils.arg('--storage', metavar='<STORAGE>', required=True, help='ID or name of target storage')
def do_disk_migrate(client, args):
    """ migrate a disk """
    disk = client.disks.perform_action(args.id, 'migrate',
                                    storage_id=args.storage)
    utils.print_dict(disk)


@utils.arg('id', metavar='<DISK_ID>', help='ID of virtual disk to show')
def do_disk_show(client, args):
    """ Show details of a virtual disk """
    disk = client.disks.get(args.id)
    utils.print_dict(disk)


@utils.arg('id', metavar='<DISK_ID>', help='ID of virtual disk to show')
@utils.arg('--tenant', metavar='<TENANT>', required=True, help='Target tenant')
@utils.arg('--user', metavar='<USER>', required=True, help='Target user')
def do_disk_change_owner(client, args):
    """ Show details of a virtual disk """
    kwargs = {}
    kwargs['tenant'] = args.tenant
    kwargs['user'] = args.user
    disk = client.disks.perform_action(args.id, 'change-owner', **kwargs)
    utils.print_dict(disk)


@utils.arg('id', metavar='<DISK_ID>', help='ID of virtual disk to restore')
@utils.arg('timestamp', metavar='<TIMESTAMP>', help='Timestamp of snapshot')
@utils.arg('--src-disk', metavar='<DISK_ID>', help='ID of source virtual disk snapshot to restore')
def do_disk_restore_snapshot(client, args):
    """ Restore of a virtual disk from snapshot """
    kwargs = {}
    kwargs['timestamp'] = args.timestamp
    if args.src_disk:
        kwargs['disk'] = args.src_disk
    disk = client.disks.perform_action(args.id, 'restore-snapshot', **kwargs)
    utils.print_dict(disk)


@utils.arg('id', metavar='<DISK_ID>', help='ID of virtual disk to get metadata info')
@utils.arg('--field', metavar='<METADATA_FIELD>', help='Field name of metadata')
def do_disk_metadata(client, args):
    """ Show metadata info of a virtual disk """
    kwargs = {}
    if args.field is not None:
        kwargs['field'] = args.field
    disk = client.disks.get_metadata(args.id, **kwargs)
    if isinstance(disk, dict):
        utils.print_dict(disk)
    else:
        print(disk)
