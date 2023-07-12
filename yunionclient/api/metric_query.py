from collections import OrderedDict

class MetricQuery(object):

    def __init__(self, measurement, field, alias, idkey, idvalue, aggr_func='mean'):
        self.id_key = idkey
        self.id_value = idvalue
        self.measurement = measurement
        self.field = field
        self.alias = alias
        self.aggr_func = aggr_func

    def query(self):
        if (isinstance(self.id_value, list)):
            op = "=~"
            val = "/" + "|".join(self.id_value) + "/"
        else:
            op = "="
            val = self.id_value
        return {
            "measurement": self.measurement,
            "select": [
                [
                    {
                        "type": "alias",
                        "params": [self.alias],
                    },
                    {
                        "type": "field",
                        "params": [self.field],
                    },
                    {
                        "type": self.aggr_func,
                        "params": [],
                    },
                ],
            ],
            "tags": [
                {
                    "key": self.id_key,
                    "value": val,
                    "operator": op,
                },
            ],
            "group_by": [
                {
                    "type": "tag",
                    "params": [self.id_key],
                },
            ],
        }

def jsonify(q):
    import json
    return json.dumps(q, sort_keys=True, ensure_ascii=False, separators=(',', ':'))

def monitor_signature(q):
    if hasattr(q, "signature"):
        del q["signature"]
    q = sorted_dict(q)
    import hashlib
    body = jsonify(q)
    q["signature"] = hashlib.sha256(body.encode("utf-8")).hexdigest()
    # body = jsonify(q)
    return q

class Query(object):

    def __init__(self, src, interval):
        self.src = src
        self.interval = interval
        self.scope = "system"
        self.unit = False
        self.metrics = []

    def add_metric(self, measurement, field, alias, idkey, idvalue):
        self.metrics.append(MetricQuery(measurement, field, alias, idkey, idvalue))

    def query(self):
        metrics =[]
        for i in range(len(self.metrics)):
            metrics.append({"model": self.metrics[i].query()})
        q = {
            "metric_query": metrics,
            "scope": self.scope,
            "from": self.src,
            "interval": self.interval,
            "unit": self.unit,
        }
        return monitor_signature(q)

def sorted_dict(q):
    if isinstance(q, dict):
        ret = OrderedDict()
        myKeys = list(q.keys())
        myKeys.sort()
        for k in myKeys:
            ret[k] = sorted_dict(q[k])
        return ret
    elif isinstance(q, list):
        ret = []
        sorted(q, key=jsonify)
        for i in range(len(q)):
            ret.append(sorted_dict(q[i]))
        return ret
    else:
        return q

if __name__ == '__main__':
    q = Query("24h", "5m")
    q.add_metric("vm_diskio", "read_bps", "磁盘读速率", "vm_id", "ab9502de-c6b6-4150-880b-d0e3e6ba8ec8")
    print(jsonify(q.query()))
    q.add_metric("vm_diskio", "read_bps", "磁盘读速率", "vm_id", ["ab9502de-c6b6-4150-880b-d0e3e6ba8ec8", "ab9502de-c6b6-4150-880b-d0e3e6ba8ec9"])
    print(jsonify(q.query()))
