from yunionclient.common import utils

@utils.arg('--tenant', metavar='<TENANT>', help='Tenant Name')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_monitor_alive_check_list(client, args):
    """ List monitor items """
    kwargs = {}
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.system:
        kwargs['is_system'] = True

    monitors = client.alivecheck.list(**kwargs)
    utils.print_list(monitors, client.alivecheck.columns)

@utils.arg('--server-id', metavar='<SERVER>', required=True, help='Server ID')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant Name')
@utils.arg('--description', metavar='<DESCRIPTION>', help='Description')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_monitor_alive_check_create(client, args):
    """ Create alive check monitor """
    kwargs = {'server_id': args.server_id}
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.description:
        kwargs['description'] = args.description
    if args.system:
        kwargs['is_system'] = True
    item = client.alivecheck.create(**kwargs)
    utils.print_dict(item)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_alive_check_enable(client, args):
    """ enable alive check monitor """
    item = client.alivecheck.perform_action(args.id, 'enable')
    utils.print_dict(item)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_alive_check_disable(client, args):
    """  disable alive check monitor """
    item = client.alivecheck.perform_action(args.id, 'disable')
    utils.print_dict(item)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_alive_check_delete(client, args):
    """ Delete alive check monitor """
    item = client.alivecheck.delete(args.id)
    utils.print_dict(item)

@utils.arg('--tenant', metavar='<TENANT>', help='Tenant Name')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_monitor_tcp_check_list(client, args):
    """ List monitor items """
    kwargs = {}
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.system:
        kwargs['is_system'] = True

    monitors = client.tcpcheck.list(**kwargs)
    utils.print_list(monitors, client.tcpcheck.columns)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_tcp_check_enable(client, args):
    """ Enable tcp check monitor """
    item = client.tcpcheck.perform_action(args.id, 'enable')
    utils.print_dict(item)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_tcp_check_disable(client, args):
    """ Disable tcp check monitor """
    item = client.tcpcheck.perform_action(args.id, 'disable')
    utils.print_dict(item)

@utils.arg('--server-id', metavar='<SERVER>', required=True, help='Server ID')
@utils.arg('--tcp-port', metavar='<TCPPORT>', required=True, help='TCP port')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant Name')
@utils.arg('--description', metavar='<DESCRIPTION>', help='Description')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_monitor_tcp_check_create(client, args):
    """ Create tcp check monitor """
    kwargs = {
            'server_id': args.server_id,
            'port': args.tcp_port,
            }
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.description:
        kwargs['description'] = args.description
    if args.system:
        kwargs['is_system'] = True

    item = client.tcpcheck.create(**kwargs)
    utils.print_dict(item)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_tcp_check_delete(client, args):
    """ Delete tcp check monitor """
    item = client.tcpcheck.delete(args.id)
    utils.print_dict(item)

@utils.arg('--tenant', metavar='<TENANT>', help='Tenant Name')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_monitor_metric_check_list(client, args):
    """ List monitor items """
    kwargs = {}
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.system:
        kwargs['is_system'] = True

    monitors = client.metriccheck.list(**kwargs)
    utils.print_list(monitors, client.metriccheck.columns)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_metric_check_enable(client, args):
    """ Enable metric check monitor """
    item = client.metriccheck.perform_action(args.id, 'enable')
    utils.print_dict(item)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_metric_check_disable(client, args):
    """ Disable metric check monitor """
    item = client.metriccheck.perform_action(args.id, 'disable')
    utils.print_dict(item)

@utils.arg('--server-id', metavar='<SERVER>', required=True, help='Server ID')
@utils.arg('--metric', metavar='<METRIC>', required=True, help='Metric Key')
@utils.arg('--threshold', metavar='<THRESHOLD>', required=True, help='Threshold')
@utils.arg('--operator', metavar='<OPERATOR>', choices=['GT', 'EQ', 'LT'], required=True, help='Operator')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant Name')
@utils.arg('--description', metavar='<DESCRIPTION>', help='Description')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_monitor_metric_check_create(client, args):
    """ Create metric check monitor """
    kwargs = {
            'server_id': args.server_id,
            'metric': args.metric,
            'threshold': args.threshold,
            'operator': args.operator,
            }
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.description:
        kwargs['description'] = args.description
    if args.system:
        kwargs['is_system'] = True

    item = client.metriccheck.create(**kwargs)
    utils.print_dict(item)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_metric_check_delete(client, args):
    """ Delete metric check monitor """
    item = client.metriccheck.delete(args.id)
    utils.print_dict(item)

@utils.arg('--tenant', metavar='<TENANT>', help='Tenant Name')
@utils.arg('--server-id', metavar='<SERVER>', help='Server ID')
@utils.arg('--group-id', metavar='<GROUP>', help='Group ID')
@utils.arg('--system', action='store_true', help='Show system objects?')
@utils.arg('--mtype', metavar='<TYPE>', choices=['server', 'redis', 'rds', 'elb'], help='Metric type')
def do_monitor_metrics_list(client, args):
    """ List available metrics """
    kwargs = {}
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.server_id:
        kwargs = {'server_id': args.server_id}
    if args.group_id:
        kwargs = {'group_id': args.group_id}
    if args.system:
        kwargs['is_system'] = True
    if args.mtype:
        kwargs['type'] = args.mtype
    metrics = client.metrics.list(**kwargs)
    utils.print_list(metrics, client.metrics.columns)

@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant Name')
@utils.arg('--id', metavar='<ID>', help='Monitor Item ID')
@utils.arg('--server-id', metavar='<SERVER>', help='Server ID')
@utils.arg('--time-from', metavar='<TIMEFROM>', help='Time from')
@utils.arg('--time-till', metavar='<TIMETILL>', help='Time till')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_monitor_event_list(client, args):
    """List event history"""
    kwargs = {}
    if args.id:
        kwargs['monitorid'] = args.id
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.server_id:
        kwargs['server_id'] = args.server_id
    if args.time_from and args.time_till:
        kwargs['time_from'] = args.time_from
        kwargs['time_till'] = args.time_till
    if args.limit:
        kwargs['limit'] = args.limit
    if args.offset:
        kwargs['offset'] = args.offset
    if args.order:
        kwargs['order'] = args.order
    if args.system:
        kwargs['is_system'] = True
    events = client.eventhistory.list(**kwargs)
    utils.print_list(events, client.eventhistory.columns)

@utils.arg('userid', metavar='<USER>', help='USER ID')
def do_monitor_media_list(client, args):
    """List media"""
    kwargs = {'user_id': args.userid}
    medias = client.media.list(**kwargs)
    utils.print_list(medias)

@utils.arg('--user-id', metavar='<USER>', required=True, help='User monitor ID')
@utils.arg('--email', metavar='<EMAIL>', help='Email send to')
@utils.arg('--sms', metavar='<SMS>', help='SMS number send to')
def do_monitor_media_create(client, args):
    """Create user media"""
    kwargs = {'user_id': args.user_id}
    if args.email:
        kwargs['email'] = args.email
    if args.sms:
        kwargs['sms'] = args.sms

    media = client.media.create(**kwargs)
    utils.print_dict(media)

@utils.arg('id', metavar='<MEDIA>', help='Media ID')
def do_monitor_media_delete(client, args):
    """Delete user media"""
    media = client.media.delete(args.id)
    utils.print_dict(media)

@utils.arg('--instance-id', metavar='<INSTANCE>', required=True, help='Instance ID')
@utils.arg('--metric', metavar='<METRIC_KEY>', required=True, help='Metric key')
@utils.arg('--mtype', metavar='<MONITOR_TYPE>', required=True, choices=['server', 'rds', 'redis', 'elb'], help='Instance type')
@utils.arg('--since', metavar='<SINCE>', help='since time')
@utils.arg('--until', metavar='<UNTIL>', help='util time')
@utils.arg('--stat_func', metavar='<FUNC>', choices=['max', 'min', 'sum', 'avg'], help='value function')
@utils.arg('--interval_unit', required=False,
           help='Specify time unit for INTERVAL argument.',
           default='minute', choices=['minute', 'hour', 'day'])
@utils.arg('--count', required=False,\
           help='How many items to be returned; Default is 20.', default=20)
def do_monitor_data(client, args):
    """ List monitor data """
    kwargs = {}
    kwargs['instance_id'] = args.instance_id
    kwargs['metric'] = args.metric
    kwargs['mtype'] = args.mtype
    if args.since:
        kwargs['since'] = args.since
    if args.until:
        kwargs['until'] = args.until
    if args.stat_func:
        kwargs['stat_func'] = args.stat_func
    if args.interval_unit:
        kwargs['interval_unit'] = args.interval_unit
    if args.count:
        kwargs['count'] = args.count
    datas = client.datahistory.list(**kwargs)
    utils.print_list(datas, client.datahistory.columns)

@utils.arg('--redis-id', metavar='<REDIS_ID>', required=True, help='Redis ID')
@utils.arg('--metric', metavar='<METRIC>', required=True, help='Metric Key')
@utils.arg('--threshold', metavar='<THRESHOLD>', required=True, help='Threshold')
@utils.arg('--operator', metavar='<OPERATOR>', choices=['GT', 'EQ', 'LT'], required=True, help='Operator')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant Name')
@utils.arg('--description', metavar='<DESCRIPTION>', help='Description')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_monitor_redis_check_create(client, args):
    """ Create redis check monitor """
    kwargs = {
            'group_id': args.redis_id,
            'metric': args.metric,
            'threshold': args.threshold,
            'operator': args.operator,
            }
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.description:
        kwargs['description'] = args.description
    if args.system:
        kwargs['is_system'] = True

    item = client.redischeck.create(**kwargs)
    utils.print_dict(item)

@utils.arg('--tenant', metavar='<TENANT>', help='Tenant Name')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_monitor_redis_check_list(client, args):
    """ List monitor items """
    kwargs = {}
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.system:
        kwargs['is_system'] = True

    monitors = client.redischeck.list(**kwargs)
    utils.print_list(monitors, client.redischeck.columns)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_redis_check_enable(client, args):
    """ Enable redis check monitor """
    item = client.redischeck.perform_action(args.id, 'enable')
    utils.print_dict(item)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_redis_check_disable(client, args):
    """ Disable redis check monitor """
    item = client.redischeck.perform_action(args.id, 'disable')
    utils.print_dict(item)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_redis_check_delete(client, args):
    """ Delete redis check monitor """
    item = client.redischeck.delete(args.id)
    utils.print_dict(item)

@utils.arg('--redis-id', metavar='<REDIS_ID>', required=True, help='Redis ID')
@utils.arg('--metric', metavar='<METRIC>', required=True, help='Metric Key')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant Name')
@utils.arg('--description', metavar='<DESCRIPTION>', help='Description')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_monitor_redis_alive_check_create(client, args):
    """ Create redis alive check monitor """
    kwargs = {
            'group_id': args.redis_id,
            'metric': args.metric,
            }
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.description:
        kwargs['description'] = args.description
    if args.system:
        kwargs['is_system'] = True

    item = client.redisalivecheck.create(**kwargs)
    utils.print_dict(item)

@utils.arg('--tenant', metavar='<TENANT>', help='Tenant Name')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_monitor_redis_alive_check_list(client, args):
    """ List monitor items """
    kwargs = {}
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.system:
        kwargs['is_system'] = True

    monitors = client.redisalivecheck.list(**kwargs)
    utils.print_list(monitors, client.redisalivecheck.columns)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_redis_alive_check_delete(client, args):
    """ Delete redis alive check monitor """
    item = client.redisalivecheck.delete(args.id)
    utils.print_dict(item)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_redis_alive_check_enable(client, args):
    """ Enable redis alive check monitor """
    item = client.redisalivecheck.perform_action(args.id, 'enable')
    utils.print_dict(item)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_redis_alive_check_disable(client, args):
    """ Disable redis alive check monitor """
    item = client.redisalivecheck.perform_action(args.id, 'disable')
    utils.print_dict(item)

@utils.arg('--mss-id', metavar='<MSS_ID>', required=True, help='MSS ID, UserID')
@utils.arg('--metric', metavar='<METRIC>', required=True, help='Metric Key')
@utils.arg('--threshold', metavar='<THRESHOLD>', required=True, help='Threshold')
@utils.arg('--operator', metavar='<OPERATOR>', choices=['GT', 'EQ', 'LT'], required=True, help='Operator')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant Name')
@utils.arg('--description', metavar='<DESCRIPTION>', help='Description')
#@utils.arg('--system', action='store_true', help='Show system objects?')
def do_monitor_mss_check_create(client, args):
    """ Create mss check monitor """
    kwargs = {
            'group_id': args.mss_id,
            'metric': args.metric,
            'threshold': args.threshold,
            'operator': args.operator,
            }
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.description:
        kwargs['description'] = args.description
    #if args.system:
    #    kwargs['is_system'] = True

    item = client.msscheck.create(**kwargs)
    utils.print_dict(item)

@utils.arg('--tenant', metavar='<TENANT>', help='Tenant Name')
#@utils.arg('--system', action='store_true', help='Show system objects?')
def do_monitor_mss_check_list(client, args):
    """ List monitor items """
    kwargs = {}
    if args.tenant:
        kwargs['tenant'] = args.tenant
    #if args.system:
    #    kwargs['is_system'] = True

    monitors = client.msscheck.list(**kwargs)
    utils.print_list(monitors, client.msscheck.columns)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_mss_check_enable(client, args):
    """ Enable mss check monitor """
    item = client.msscheck.perform_action(args.id, 'enable')
    utils.print_dict(item)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_mss_check_disable(client, args):
    """ Disable mss check monitor """
    item = client.msscheck.perform_action(args.id, 'disable')
    utils.print_dict(item)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_mss_check_delete(client, args):
    """ Delete mss check monitor """
    item = client.msscheck.delete(args.id)
    utils.print_dict(item)

@utils.arg('--rds-id', metavar='<RDS_ID>', required=True, help='RDS ID')
@utils.arg('--metric', metavar='<METRIC>', required=True, help='Metric Key')
@utils.arg('--threshold', metavar='<THRESHOLD>', required=True, help='Threshold')
@utils.arg('--operator', metavar='<OPERATOR>', choices=['GT', 'EQ', 'LT'], required=True, help='Operator')
@utils.arg('--tenant', metavar='<TENANT>', help='Tenant Name')
@utils.arg('--description', metavar='<DESCRIPTION>', help='Description')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_monitor_rds_check_create(client, args):
    """ Create rds check monitor """
    kwargs = {
            'group_id': args.rds_id,
            'metric': args.metric,
            'threshold': args.threshold,
            'operator': args.operator,
            }
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.description:
        kwargs['description'] = args.description
    if args.system:
        kwargs['is_system'] = True

    item = client.rdscheck.create(**kwargs)
    utils.print_dict(item)

@utils.arg('--tenant', metavar='<TENANT>', help='Tenant Name')
@utils.arg('--system', action='store_true', help='Show system objects?')
def do_monitor_rds_check_list(client, args):
    """ List monitor items """
    kwargs = {}
    if args.tenant:
        kwargs['tenant'] = args.tenant
    if args.system:
        kwargs['is_system'] = True

    monitors = client.rdscheck.list(**kwargs)
    utils.print_list(monitors, client.rdscheck.columns)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_rds_check_enable(client, args):
    """ Enable rds check monitor """
    item = client.rdscheck.perform_action(args.id, 'enable')
    utils.print_dict(item)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_rds_check_disable(client, args):
    """ Disable rds check monitor """
    item = client.rdscheck.perform_action(args.id, 'disable')
    utils.print_dict(item)

@utils.arg('id', metavar='<ID>', help='Monitor Item ID')
def do_monitor_rds_check_delete(client, args):
    """ Delete rds check monitor """
    item = client.rdscheck.delete(args.id)
    utils.print_dict(item)

@utils.arg('--tenant', metavar='<TENANT>', help='Tenant')
def do_monitor_check_summary(client, args):
    """ Count"""
    kwargs = {}
    if args.tenant:
        kwargs['tenant'] = args.tenant
    counts = client.checksummary.list(**kwargs)
    utils.print_list(counts, client.checksummary.columns)
