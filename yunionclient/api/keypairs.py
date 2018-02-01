from yunionclient.common import base


class KeypairManager(base.StandaloneManager):
    keyword = 'keypair'
    keyword_plural = 'keypairs'
    _columns = ['ID', 'Name', 'Scheme', 'Fingerprint', 'Created_at', 'Private_key_len',
            'Description', 'Linked_guest_count']
