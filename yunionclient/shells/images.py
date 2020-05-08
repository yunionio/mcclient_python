from yunionclient.common import utils

@utils.arg('--owner-id', metavar='<OWNER>', help='Tenant id of image owner')
@utils.arg('--tenant', metavar='<TENANT>', help='Image owner')
@utils.arg('--is-public', metavar='<IS_PUBLIC>', choices=['True', 'False', 'None', 'true', 'false', 'none'], help='filter images public or not(True, False or None)')
@utils.arg('--admin', action='store_true', help='Show images of all tenants, ADMIN only')
@utils.arg('--limit', metavar='<LIMIT>', default=0, help='Max items show, 0 means no limit')
@utils.arg('--marker', metavar='<MARKER>', help='The last Image ID of the previous page')
@utils.arg('--history', action='store_true', help='Show images with all history')
@utils.arg('--name', metavar='<NAME>', help='Name filter')
def do_image_list(client, args):
    """ List images in glance """
    kwargs = {}
    if not args.admin and not args.tenant and not args.owner_id:
        if client.default_tenant.is_system_admin():
            kwargs['owner'] = client.default_tenant.get_id()
    else:
        if not client.default_tenant.is_system_admin():
            raise Exception('System admin ONLY option')
        if args.tenant:
            t = client.tenants.get(args.tenant)
            kwargs['owner'] = t.id
        elif args.owner_id is not None:
            kwargs['owner'] = args.owner_id

    if args.is_public is not None:
        kwargs['is_public'] = args.is_public

    if args.name:
        kwargs['name'] = args.name

    if args.marker is not None:
        kwargs['marker'] = args.marker

    kwargs['limit'] = args.limit

    if args.history is not None and args.history:
        kwargs['history'] = args.history

    images = client.images.list(**kwargs)
    utils.print_list(images, client.images.columns)


@utils.arg('id', metavar='<IMAGE_ID>', help='ID of image to update')
def do_image_show(client, args):
    """ Show details of a image """
    image = client.images.get(args.id)
    utils.print_dict(image)


@utils.arg('id', metavar='<IMAGE_ID>', help='ID of image to update')
@utils.arg('--name', metavar='<IMAGE_NAME>', help='Name of image to update')
@utils.arg('--public', action='store_true', help='Make public')
@utils.arg('--private', action='store_true', help='Make private')
@utils.arg('--format', metavar='<IMAGE_FORMAT>', choices=['raw', 'qcow2', 'iso'], help='Format of image')
@utils.arg('--min-disk', metavar='<MIN_DISK_SIZE_MB>', type=int, help='Disk size after expanded, in MB')
@utils.arg('--min-ram', metavar='<MIN_RAM_MB>', type=int, help='Minimal memory size required')
def do_image_update(client, args):
    """ Update a disk image on glance server """
    img = client.images.get(args.id)
    kwargs = {}
    if args.name is not None and args.name != img.name:
        kwargs['name'] = args.name
    if args.public and not utils.ensure_bool(img.is_public):
        kwargs['is-public'] = 'true'
    elif args.private and utils.ensure_bool(img.is_public):
        kwargs['is-public'] = 'false'
    if args.format is not None and args.format != img.disk_format:
        kwargs['disk-format'] = args.format
    if args.min_disk is not None and args.min_disk > 0:
        kwargs['min-disk'] = '%s' % args.min_disk
    if args.min_ram is not None and args.min_ram > 0:
        kwargs['min-ram'] = '%s' % args.min_ram
    if len(kwargs) == 0:
        raise Exception('No data to update')
    image = client.images.update(img.id, kwargs)
    utils.print_dict(image)


@utils.arg('id', metavar='<IMAGE_ID>', help='ID of image to update')
@utils.arg('--os-type', metavar='<OS_TYPE>', choices=['Windows', 'Linux', 'Freebsd', ''], help='Type of OS')
@utils.arg('--os-distribution', metavar='<OS_DISTRIBUTION>', help='Distribution of OS')
@utils.arg('--os-version', metavar='<OS_VERSION>', help='Version of OS')
@utils.arg('--os-codename', metavar='<OS_CODENAME>', help='Codename of OS')
@utils.arg('--os-arch', metavar='<OS_ARCH>', choices=['i386', 'x86_64', ''], help='Distribution of OS')
@utils.arg('--preference', metavar='<PREFERENCE>', help='Disk preferences')
@utils.arg('--notes', metavar='<NOTES>', help='Notes')
def do_image_update_property(client, args):
    """ Update a disk image on glance server """
    img = client.images.get(args.id)
    kwargs = img.properties
    if args.os_distribution is not None:
        if len(args.os_distribution) == 0:
            kwargs.pop('os_distribution', None)
        else:
            kwargs['os_distribution'] = args.os_distribution
    if args.os_version is not None:
        if len(args.os_version) == 0:
            kwargs.pop('os_version', None)
        else:
            kwargs['os_version'] = args.os_version
    if args.os_codename is not None:
        if len(args.os_codename) == 0:
            kwargs.pop('os_codename', None)
        else:
            kwargs['os_codename'] = args.os_codename
    if args.os_arch is not None:
        if len(args.os_arch) == 0:
            kwargs.pop('os_arch', None)
        else:
            kwargs['os_arch'] = args.os_arch
    if args.preference is not None:
        if len(args.preference) == 0:
            kwargs.pop('preference', None)
        else:
            kwargs['preference'] = args.preference
    if args.os_type is not None:
        if len(args.os_type) == 0:
            kwargs.pop('os_type', None)
        else:
            kwargs['os_type'] = args.os_type
    if args.notes is not None:
        if len(args.notes) == 0:
            kwargs.pop('notes', None)
        else:
            if isinstance(args.notes, str):
                notes = args.notes.encode('utf-8')
            else:
                notes = args.notes
            kwargs['notes'] = notes
    image = client.images.update_properties(img.id, **kwargs)
    utils.print_dict(image)


def do_docker_image_upload(client, args):
    """
    upload docker image from bottom to top, print_dict the top image info
    """
    from yunionclient.api import glanceutils
    import subprocess
    (layers, tmp_file) = glanceutils.get_image_layers(args.file)
    image = None
    for layer in reversed(layers):
        # layer format {'id': <layer-id>, 'pid': <layer's parent id>,
        # 'file': <path of the tar>, 'name': <name of image, if exists>}
        image = client.images.get_image_by_docker_id(layer['id'])
        if len(image) == 1:
            #print 'got same image on glance, skip to continue'
            continue
        kwargs = {}
        kwargs['docker_id'] = layer['id']
        kwargs['docker_parent_id'] = layer['pid']
        if layer == layers[0]:
            # if it's the top layer, use the specified name cover the layer's original name
            layer['name'] = args.name
            if args.tag:
                # if has tag, assign to it
                kwargs['tag'] = args.tag

        image = client.images.upload(layer['file'], layer['name'], 'docker', args.public,
                                     kwargs)
    subprocess.check_call(['sudo', 'rm', '-rf', tmp_file])
    utils.print_dict(image)


@utils.arg('name', metavar='<IMAGE_NAME>', help='Name of image to update')
@utils.arg('--public', action='store_true', help='Make image public, default is private')
@utils.arg('--format', metavar='<IMAGE_FORMAT>', required=True, choices=['raw', 'qcow2', 'iso', 'vmdk', 'docker'], help='Format of image')
@utils.arg('--file', metavar='<IMAGE_FILE_PATH>', required=True, help='Path of image file or ID of docker image')
@utils.arg('--use-id', metavar='<REPLACE_IMAGE_ID>', help='Existing image ID to replace')
@utils.arg('--tag', metavar='<IMAGE_TAG>', help='Image TAG')
def do_image_upload(client, args):
    if args.format == 'docker':
        do_docker_image_upload(client, args)
    else:
        """ Upload a image from a local file """
        replace_img = None
        if args.use_id:
            replace_img = client.images.get(args.use_id)
        img = client.images.upload(args.file, args.name, args.format, args.public)
        # if upload common image, then replace_img only judge once. if upload docker, replace_img should be None.
        if replace_img:
            client.images.swap_location(replace_img.id, img.id)
            img = client.images.get(replace_img.id)
        utils.print_dict(img)


@utils.arg('id1', metavar='<IMAGE_NAME>', help='Name of image 1 to swap location')
@utils.arg('id2', metavar='<IMAGE_NAME>', help='Name of image 2 to swap location')
def do_image_swap_locations(client, args):
    """ Swap locations between two images """
    img1 = client.images.get(args.id1)
    img2 = client.images.get(args.id2)
    client.images.swap_location(img1.id, img2.id)


@utils.arg('id', metavar='<IMAGE_ID>', help='ID of image to update')
def do_image_delete(client, args):
    """ Delete a image disk from glance server """
    id = args.id
    while id:
        img = client.images.get(id)
        ret = client.images.delete(img.id)
        if ret and ret.get('has_sons'):
            # if the image has sons, then stop deleting.
            #print 'image %s has sons, stop delete' % img.id
            break
        if ret and len(ret.get('parent_image')) > 0:
            parent_image = ret.get('parent_image')[0]  # assume only one parent exist
            # if arrives at a image has a name, if it's not the top image,
            # we should stop deleting.
            if parent_image.get('name'):
                #print 'stop deleting at image %s' % parent_image.get('id')
                break
        if hasattr(img, 'parent_id'):
            id = img.parent_id
        else:
            id = None


@utils.arg('id', metavar='<IMAGE_ID>', help='ID of image to update')
@utils.arg('--output', metavar='<OUTPUT_FILE>', help='Save image to file')
def do_image_download(client, args):
    """ Download a image disk from glance server """
    img = client.images.get(args.id)
    if img['disk_format'] == 'docker':
        """ Download docker image """
        image_history = client.images.get_image_history(img['id'])
        from yunionclient.api import glanceutils
        import subprocess
        tmp_file = []
        for image in reversed(image_history):
            if glanceutils.search_image_in_local(image['docker_id']):
                continue
            image_path = '/tmp/' + image['docker_id'] + '.tar'
            tmp_file.append(image_path)
            client.images.download(image['id'], image_path)
            glanceutils.load_image(image_path)
        for file in tmp_file:
            subprocess.check_call(['sudo', 'rm', '-rf', file])
    else:
        client.images.download(img.id, args.output)


@utils.arg('id', metavar='<IMAGE_ID>', help='ID of image to update')
@utils.arg('--tag', metavar='<IMAGE_TAG>', help='Image TAG')
def do_image_add_tag(client, args):
    if not args.tag:
        raise Exception('No tag specified')
    img = client.images.get(args.id)
    client.images.add_tag(img.id, args.tag)


@utils.arg('id', metavar='<IMAGE_ID>', help='ID of image to update')
@utils.arg('--tag', metavar='<IMAGE_TAG>', help='Image TAG')
def do_image_delete_tag(client, args):
    if not args.tag:
        raise Exception('No tag specified')
    img = client.images.get(args.id)
    client.images.delete_tag(img.id, args.tag)

