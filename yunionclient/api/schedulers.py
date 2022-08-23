from yunionclient.common import base


class SchedulerManager(base.SchedulerManager):
    keyword = 'scheduler'
    keyword_plural = 'schedulers'
    _columns = []

    def forecast(self, count, **kwargs):
        url = r'/scheduler/forecast'
        kwargs['__count__'] = count
        resp, body = self.json_request('POST', url, body=kwargs)
        return body

    def history(self, **kwargs):
        url = r'/scheduler/history-list'
        return self._create(url, kwargs, "data")

    def history_show(self, idstr, **kwargs):
        url = r'/scheduler/history-detail/%s' % (idstr)
        return self._create(url, kwargs, "history")
