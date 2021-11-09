import yunionclient

from yunionclient.common import utils

def do_capabilities(client, args):
    """ Show capabilities """
    kwargs = {}
    capa = client.capabilities.list(**kwargs)
    utils.print_dict(capa)



