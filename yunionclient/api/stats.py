from yunionclient.common.base import Manager


class StatsManager(Manager):

    def get(self):
        resp, body = self.json_request('GET', '/stats')
        return body


class RegionStatsManager(StatsManager):
    service_type = 'compute'
