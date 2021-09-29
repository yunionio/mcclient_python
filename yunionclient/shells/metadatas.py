from yunionclient.common import utils


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--admin', action='store_true', help='Is admin call?')
@utils.arg('--sys-meta', action='store_true', help='Show sys metadata only')
@utils.arg('--user-meta', action='store_true', help='Show user metadata only')
@utils.arg('--cloud-meta', action='store_true', help='Show cloud metadata only')
@utils.arg('--service', metavar='<SERVICE>', help='Show services metadatas')
def do_metadata_list(client, args):
    """ List all metadata """
    kwargs = {}
    if args.limit:
        kwargs['limit'] = args.limit
    if args.offset:
        kwargs['offset'] = args.offset
    if args.admin:
        kwargs['admin'] = True
    if args.sys_meta:
        kwargs['sys_meta'] = True
    if args.user_meta:
        kwargs['user_meta'] = True
    if args.cloud_meta:
        kwargs['cloud_meta'] = True
    if args.service:
        kwargs['service'] = args.service
    metadatas = client.metadatas.list(**kwargs)
    utils.print_list(metadatas, client.metadatas.columns)

@utils.arg('id', metavar='<METADATA_ID>', help='ID of metadata to update')
@utils.arg('--service', metavar='<SERVICE>', help='Show services metadatas')
def do_metadata_show(client, args):
    """ Show details of a metadata """
    kwargs = {}
    if args.service:
        kwargs['service'] = args.service
    metadata = client.metadatas.get(args.id, **kwargs)
    utils.print_dict(metadata)


