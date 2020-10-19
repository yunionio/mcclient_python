from yunionclient.common import utils

@utils.arg('brand', metavar='<BRAND>', help='brand of vm')
@utils.arg('instance_type', metavar='<SKU>', help='sku of instance')
@utils.arg('disk_type', metavar='<DISK_TYPE>', help='disk type of instance')
@utils.arg('disk_size_gb', metavar='<DISK_SIZE_GB>', help='disk size in db')
@utils.arg('--region', metavar='<REGION>', help='Region of instance')
@utils.arg('--zone', metavar='<ZONE>', help='Zone of instance')
def do_instance_price(client, args):
    """ get price of an instance """
    from yunionclient.api.price_infos import InstanceSpec
    spec = InstanceSpec(args.brand, args.region, args.zone, args.instance_type, args.disk_type, args.disk_size_gb)
    info = client.price_infos.get_price(spec.get_specs())
    utils.print_dict(info)
