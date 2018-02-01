from yunionclient.common import base


class RateManager(base.StandaloneManager):
    service_type = 'meter'
    keyword = 'rate'
    keyword_plural = 'rates'

    def get_rate_table_at(self, tm):
        assert(tm is not None and len(tm) > 0)
        url = r'/rates/%s' % (tm)
        return self._get(url, self.keyword_plural)

    def get_rate_tables_between(self, start, end):
        assert(start is not None and len(start) > 0)
        if end is None or len(end) == 0:
            end = '-'
        url = r'/rates/%s/%s' % (start, end)
        return self._get(url, self.keyword_plural)

    def get_rates_at(self, res_type, sub_res_id, time):
        if sub_res_id is None or len(sub_res_id) == 0:
            sub_res_id = '-'
        if time is None or len(time) == 0:
            time = '-'
        url = r'/rates/%s/%s/%s' % (res_type, sub_res_id, time)
        return self._get(url, self.keyword)

    def get_rates_between(self, res_type, sub_res_id, tm1, tm2):
        if sub_res_id is None or len(sub_res_id) == 0:
            sub_res_id = '-'
        if tm1 is None:
            tm1 = '-'
        if tm2 is None:
            tm2 = '-'
        url = r'/rates/%s/%s/%s/%s' % (res_type, sub_res_id, tm1, tm2)
        return self._get(url, self.keyword_plural)

    def update_rate(self, res_type, sub_res_id, tm, **kwargs):
        if sub_res_id is None or len(sub_res_id) == 0:
            sub_res_id = '-'
        url = r'/rates/%s/%s/%s' % (res_type, sub_res_id, tm)
        body = {self.keyword: kwargs}
        return self._update(url, body, self.keyword)

    def estimate(self, since, until, **kwargs):
        url = r'/rates/%s/%s' % (since, until)
        body = {self.keyword: kwargs}
        resp, body = self.json_request('POST', url, body=body)
        return self._dict_to_object(body[self.keyword], None)
