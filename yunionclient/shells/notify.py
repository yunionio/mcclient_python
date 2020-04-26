import os.path

import yunionclient
from yunionclient.common import utils


@utils.arg('--to', metavar='<TO>', action='append', required=True, help='Notify receipient')
@utils.arg('--topic', metavar='<TOPIC>', required=True, help='Notify topic')
@utils.arg('--priority', metavar='<PRIORITY>', choices=['critical', 'important', 'normal'], help='Priority')
@utils.arg('--data', metavar='<DATA>', action='append', help='Notify data')
def do_notify(client, args):
    """ Notify message """
    kwargs = {}
    if args.data:
        for data in args.data:
            pos = data.find(':')
            if pos > 0:
                key = data[:pos]
                val = data[pos+1:]
                kwargs[key] = val
            else:
                raise Exception('Data must be key:value')
    ret = client.notify.notify(args.to, args.topic, args.priority, **kwargs)
    if ret:
        print('Delivered')
    else:
        print('Fail to deliver')

@utils.arg('--replaced', metavar='<REPLACED>', action='append', help='Replaced options of monitor info')
@utils.arg('--prefix', action='store_true', help='Enable/disable resource id prefix')
@utils.arg('region', metavar='<REGION>', help='Monitor info region')
@utils.arg('subject', metavar='<SUBJECT>', help='Monitor notify subject')
@utils.arg('body', metavar='<BODY>', help='Monitor notify body')
def do_monitor_notify(client, args):
    """ Monitor notify message """
    kwargs = {}
    kwargs['region'] = args.region
    kwargs['subject'] = args.subject
    kwargs['body'] = args.body
    if args.prefix:
        kwargs['res_id_prefix'] = True
    #print args.replaced
    replaced = []
    if args.replaced:
        for val in args.replaced:
            replaced.append(val)
    kwargs['replaced_options']  = replaced
    ret = client.notify.monitor_notify(**kwargs)
    if ret:
        print('Delivered')
    else:
        print('Fail to deliver')

@utils.arg('--user', metavar='<USER>', help='User ID or Name, only for admin')
@utils.arg('--date', metavar='<DATE>', help='UTC-Date for list quota usage and default is now, usage: yyyy-mm')
def do_notify_quota_list(client, args):
    params = {}
    if args.user is not None:
        params['user'] = args.user
    if args.date is not None:
        import re
        if not re.match(r'^\d{4}-\d{2}$', args.date):
            print('Usage: notify-quota-list [--user xx] [--date yyyy-mm]')
            return
        params['datetime'] = args.date
    items = client.notify_quota.list(**params)
    utils.print_list(items, client.notify_quota.columns)

@utils.arg('--user', metavar='<USER>', help='User ID or Name')
@utils.arg('--email', metavar='<EMAIL>', type=int, help='Quota of email')
@utils.arg('--sms', metavar='<SMS>', type=int, help='Quota of sms')
def do_notify_quota_update(client, args):
    params = {}
    if args.user is not None:
        params['user'] = args.user
    if args.email is not None:
        if args.email < 0:
            print('<EMAIL> must be positive integer')
            return
        params['email'] = args.email
    if args.sms is not None:
        if args.sms < 0:
            print('<SMS> must be positive integer')
            return
        params['sms'] = args.sms
    update_info = client.notify_quota.update(idstr=None, **params)
    utils.print_dict(update_info)


@utils.arg('id', metavar='<ID>', help='Notifycontact ID')
@utils.arg('topic', metavar='<TOPIC>', help='Topic Name')
@utils.arg('--email', metavar='<EMAIL>', choices=['on', 'off'], help='email is switched on or off')
@utils.arg('--sms', metavar='<SMS>', choices=['on', 'off'], help='sms is switched on or off')
@utils.arg('--wechat', metavar='<WECHAT>', choices=['on', 'off'], help='wechat is switched on or off')
def do_notifycontact_update_topic(client, args):
    params = {'topic': args.topic}
    if args.email is not None:
        params['email'] = args.email
    if args.sms is not None:
        params['sms'] = args.sms
    if args.wechat is not None:
        params['wechat'] = args.wechat
    item = client.notifycontacts.perform_action(args.id, 'update_topic', **params)
    utils.print_dict(item)


@utils.arg('id', metavar='<ID>', help='Notifycontact ID')
def do_notifycontact_list_topic(client, args):
    params = {}
    items = client.notifycontacts.perform_action(args.id, 'list_topic', **params)
    utils.print_list(items)


@utils.arg('--user', metavar='<USER>', help='User ID or Name, only for admin')
@utils.arg('--topic', metavar='<TOPIC>', help='Topic Name')
def do_user_topic_list(client, args):
    params = {}
    if args.user is not None:
        params['user'] = args.user
    if args.topic is not None:
        params['topic'] = args.topic
    items = client.user_topics.list(**params)
    utils.print_list(items, client.user_topics.columns)

@utils.arg('--user', metavar='<USER>', help='User ID or Name, only for admin')
@utils.arg('topic', metavar='<TOPIC>', help='Topic Name')
@utils.arg('--email', metavar='<EMAIL>', choices=['on', 'off'], help='email is switched on or off')
@utils.arg('--sms', metavar='<SMS>', choices=['on', 'off'], help='sms is switched on or off')
@utils.arg('--wechat', metavar='<WECHAT>', choices=['on', 'off'], help='wechat is switched on or off')
def do_user_topic_create(client, args):
    params = {}
    if args.user is not None:
        params['user'] = args.user
    if args.topic is not None:
        params['topic'] = args.topic

    items = client.user_topics.create(**params)
    utils.print_list(items, client.user_topics.columns)

@utils.arg('--user', metavar='<USER>', help='User ID or Name')
@utils.arg('--email', metavar='<EMAIL>', choices=['on', 'off'], help='email is switched on or off')
@utils.arg('--sms', metavar='<SMS>', choices=['on', 'off'], help='sms is switched on or off')
@utils.arg('--wechat', metavar='<WECHAT>', choices=['on', 'off'], help='wechat is switched on or off')
@utils.arg('topic', metavar='<TOPIC>', help='Topic Name')
def do_user_topic_update(client, args):
    params = {}
    params['topic'] = args.topic
    if args.user is not None:
        params['user'] = args.user
    if args.email is not None:
        params['email'] = args.email
    if args.sms is not None:
        params['sms'] = args.sms
    if args.wechat is not None:
        params['wechat'] = args.wechat
    update_info = client.user_topics.update(idstr=None, **params)
    utils.print_dict(update_info)

@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--admin', action='store_true', help='Is admin call?')
@utils.arg('--user', metavar='<USER>', help='User ID or Name')
@utils.arg('--datetime', metavar='<DATETIME>', help='List notify info recorded after datetime<YYYY-MM-DD HH:MM:SS>')
def do_notify_log_list(client, args):
    """ List all notify sending histories """
    page_info = utils.get_paging_info(args)
    if args.datetime is not None:
        page_info['datetime'] = args.datetime
    histories = client.notify_log.list(**page_info)
    utils.print_list(histories, client.notify_log.columns)

@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filters')
@utils.arg('--filter-any', action='store_true', help='If true, match if any of the filters matches; otherwise, match if all of the filters match')
@utils.arg('--admin', action='store_true', help='Is admin call?')
@utils.arg('--user', metavar='<USER>', help='User ID or Name')
@utils.arg('--datetime', metavar='<DATETIME>', help='List notify info recorded after datetime<YYYY-MM-DD HH:MM:SS>')
def do_notify_request_list(client, args):
    """ List all notify request histories """
    page_info = utils.get_paging_info(args)
    if args.datetime is not None:
        page_info['datetime'] = args.datetime
    requests = client.notify_request.list(**page_info)
    utils.print_list(requests, client.notify_request.columns)


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
def do_usercontact_list(client, args):
    """ Lease user contacts """
    page_info = utils.get_paging_info(args)
    uclist = client.notify_usercontacts.list(**page_info)
    utils.print_list(uclist, client.notify_usercontacts.columns)


@utils.arg('id', metavar='<ID>', help='User ID of Name')
def do_usercontact_show(client, args):
    """ Show details of a user """
    uc = client.notify_usercontacts.get(args.id)
    utils.print_dict(uc)


@utils.arg('id', metavar='<ID>', help='User ID or Name')
@utils.arg('contact_name', metavar='<CONTACT_NAME>', help='Name of the notify contact')
@utils.arg('--email', metavar='<EMAIL>', help='Notify contact email')
@utils.arg('--sms', metavar='<SMS>', help='Notify contact SMS')
@utils.arg('--wechat', metavar='<WECHAT>', help='Notify contact wechat')
@utils.arg('--notes', metavar='<NOTES>', help='Notify contact notes')
def do_usercontact_addnotifycontact(client, args):
    params = {'contact_name': args.contact_name}
    if args.email:
        params['email'] = args.email
    if args.sms:
        params['sms'] = args.sms
    if args.wechat:
        params['wechat'] = args.wechat
    if args.notes:
        params['notes'] = args.notes
    nc = client.notify_usercontacts.perform_action(args.id, 'addnotifycontact', **params)
    utils.print_dict(nc)


@utils.arg('id', metavar='<ID>', help='User ID or Name')
@utils.arg('notifycontact_id', metavar='<NOTIFYCONTACT_ID>', help='ID of notify contact')
def do_usercontact_removenotifycontact(client, args):
    params = {'notifycontact_id': args.notifycontact_id}
    nc = client.notify_usercontacts.perform_action(args.id, 'removenotifycontact', **params)
    utils.print_dict(nc)


@utils.arg('id', metavar='<ID>', help='User ID or Name')
def do_usercontact_listnotifycontact(client, args):
    ncs = client.notify_usercontacts.perform_action(args.id, 'listnotifycontact')
    utils.print_list(ncs)


@utils.arg('id', metavar='<ID>', help='ID of notifycontact')
@utils.arg('--email-enable', metavar='<EMAIL_ENABLE>', choices=['True', 'False'],
           help='Enable or disable the email channel')
@utils.arg('--sms-enable', metavar='<SMS_ENABLE>', choices=['True', 'False'],
           help='Enable or disable the sms channel')
@utils.arg('--wechat-enable', metavar='<WECHAT_ENABLE>', choices=['True', 'False'],
           help='Enable or disable the wechat channel')
@utils.arg('--notes', metavar='<NOTES>', help='Notify contact notes')
def do_notifycontact_update(client, args):
    """
    Only allow to enable/disable channel or edit notes
    """
    params = {}
    if args.email_enable:
        params['email_enable'] = True if args.email_enable == 'True' else False
    if args.sms_enable:
        params['sms_enable'] = True if args.sms_enable == 'True' else False
    if args.wechat_enable:
        params['wechat_enable'] = True if args.wechat_enable == 'True' else False
    if args.notes:
        params['notes'] = args.notes
    nc = client.notifycontacts.update(args.id, **params)
    utils.print_dict(nc)


@utils.arg('id', metavar='<ID>', help='ID of notify contact')
@utils.arg('channel', metavar='<CHANNEL>', help='Notify contact channel')
@utils.arg('address', metavar='<ADDRESS>', help='Notify contact channel address')
def do_notifycontact_request_verify(client, args):
    params = {
        'channel': args.channel,
        'address': args.address,
    }
    nc = client.notifycontacts.perform_action(args.id, 'request_verify', **params)
    utils.print_dict(nc)


@utils.arg('id', metavar='<ID>', help='ID of notify contact')
@utils.arg('channel', metavar='<CHANNEL>', help='Notify contact channel')
@utils.arg('token', metavar='<TOKEN>', help='Notify contact verify token')
def do_notifycontact_verify_channel(client, args):
    params = {
        'channel': args.channel,
        'token': args.token
    }
    nc = client.notifycontacts.perform_action(args.id, 'verify_channel', **params)
    utils.print_dict(nc)


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
def do_channel_list(client, args):
    """ List channels """
    page_info = utils.get_paging_info(args)
    channels = client.notify_channels.list(**page_info)
    utils.print_list(channels, client.notify_channels.columns)


@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--order-by', metavar='<ORDER_BY>', help='Name of fields order by')
@utils.arg('--order', metavar='<ORDER>', choices=['desc', 'asc'], help='order')
@utils.arg('--details', action='store_true', help='More detailed list')
@utils.arg('--search', metavar='<KEYWORD>', help='Filter result by simple keyword search')
def do_template_list(client, args):
    """ List notify templates """
    page_info = utils.get_paging_info(args)
    templates = client.notify_templates.list(**page_info)
    utils.print_list(templates, client.notify_templates.columns)


@utils.arg('id', metavar='<ID>', help='ID or name of channel')
@utils.arg('--name', metavar='<NAME>', required=True, help='Name of template to create')
@utils.arg('--title', metavar='<TITLE>', help='Title template')
@utils.arg('--body', metavar='<BODY>', required=True, help='Body template file')
@utils.arg('--signature', metavar='<SIGNATURE>', help='Signature')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
def do_channel_create_template(client, args):
    """ Create a template of a channel """
    kwargs = {}
    kwargs['name'] = args.name
    if os.path.exists(args.body):
        with open(args.body) as f:
            kwargs['body'] = f.read()
    else:
        kwargs['body'] = args.body
    if args.signature:
        kwargs['body'] += args.signature
    if args.title:
        kwargs['title'] = args.title
    if args.desc:
        kwargs['description'] = args.description
    template = client.notify_channels.create_descendent(args.id,
                    yunionclient.api.notify.templates.TemplateManager, **kwargs)
    utils.print_dict(template)


@utils.arg('id', metavar='<ID>', help='ID or name of template to show')
def do_template_show(client, args):
    """ Show details of a template """
    temp = client.notify_templates.get(args.id)
    utils.print_dict(temp)


@utils.arg('id', metavar='<ID>', help='ID or name of template to show')
@utils.arg('--name', metavar='<NAME>', help='Name of template to create')
@utils.arg('--title', metavar='<TITLE>', help='Title template')
@utils.arg('--body', metavar='<BODY>', help='Body template')
@utils.arg('--signature', metavar='<SIGNATURE>', help='Signature')
@utils.arg('--desc', metavar='<DESCRIPTION>', help='Description')
@utils.arg('--enable', action='store_true', help='Enable topic')
@utils.arg('--disable', action='store_true', help='Disable topic')
def do_template_update(client, args):
    """ Update a tempalte """
    kwargs = {}
    if args.name:
        kwargs['name'] = args.name
    if args.title:
        kwargs['title'] = args.title
    if args.body:
        if os.path.exists(args.body):
            with open(args.body) as f:
                kwargs['body'] = f.read()
        else:
            kwargs['body'] = args.body
        if args.signature:
            kwargs['body'] += args.signature
    if args.desc:
        kwargs['description'] = args.desc
    if args.enable and not args.disable:
        kwargs['enabled'] = True
    elif not args.enable and args.disable:
        kwargs['enabled'] = False
    if len(kwargs) == 0:
        raise Exception('No data to update')
    temp = client.notify_templates.update(args.id, **kwargs)
    utils.print_dict(temp)


@utils.arg('id', metavar='<ID>', help='ID or name of template to show')
def do_template_delete(client, args):
    """ Delete a template """
    temp = client.notify_templates.delete(args.id)
    utils.print_dict(temp)
