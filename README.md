YunionCloud Python Client SDK
===================================


本仓库提供了访问YunionCloud API的Python 3 SDK以及基于该SDK的climc客户端代码。


命令行使用方法
---------------


首先准备rc文件，内容如下：

    export OS_USERNAME=sysadmin
    export OS_PASSWORD=MXX2VKe067jtD
    export OS_PROJECT_NAME=system
    export OS_DOMAIN_NAME=Default
    export OS_AUTH_URL=http://10.68.22.1:5000/v3
    export OS_REGION_NAME=LocalTest


首先source该rc文件，然后执行climc，例如：

    $ source ~/rc_admin
    $ climc server-list # 列出主机
    $ climc image-list # 列出模板
    $ climc server-create --disk <image_id> --disk 40g --mem 2g --ncpu 2 --allow-delete test --hypervisor esxi # 以模板 image_id 创建主机，数据盘40g，内存2g，虚拟CPU 2核，允许删除，机器名称test，虚拟化平台为esxi (VMWare)


SDK调用方法
----------------

首先安装yunionclient，执行

    sudo python3 setup.py install

依赖安装包：

* argparse
* prettytable
* httplib2
* pycrypto>=2.6

示例代码：

    import yunionclient.api.client

    auth_url = "http://10.68.22.1:5000/v3"
    username = "sysadmin"
    password = "MXX2VKe067jtD"
    project = "system"
    domain = "Default"
    region = "LocalTest"
    timeout = 600 # 超时10分钟
    client = yunionclient.api.client.Client(auth_url,
                                        username,
                                        password,
                                        domain,
                                        region=region,
                                        timeout=timeout,
                                        insecure=True)

    if not client.set_project(project_name=project):
        raise Exception('Invalid keystone credential')

    # 列出所有模板镜像
    imgs = client.images.list(is_public='true')
    if len(imgs) <= 0:
        raise Exception('No valid image')

    # 使用第一个镜像创建一台主机
    img_id = imgs[0]['id']
    params = {}
    params['name'] = 'test'
    params['vmem_size'] = '2g' # 虚拟机内存2g
    params['vcpu_count'] = 2
    params['disk.0'] = img_id
    params['disk.1'] = '40g'
    params['hypervisor'] = 'esxi'
    guest = client.guests.create(**params)
    print 'Server created', guest

    # 开机
    client.guests.perform_action(guest['id'], 'start')

    # 删除主机
    client.guests.delete(guest['id'])
    print 'server deleted', guest





北京云联万维技术有限公司 © 2017-2020
