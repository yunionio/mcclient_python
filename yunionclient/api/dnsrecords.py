from yunionclient.common import base


class DNSRecordManager(base.StandaloneManager):
    keyword = 'dnsrecord'
    keyword_plural = 'dnsrecords'
    _columns = ['ID', 'Name', 'DnsValue', 'TTL']
