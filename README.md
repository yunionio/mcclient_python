Cloudpods Python 3 SDK
======================

本仓库提供了访问Cloudpods API的Python 3 SDK以及基于该SDK的climc客户端代码。


命令行使用方法
---------------


首先准备rc文件，内容如下(密码认证)：

    export OS_USERNAME=sysadmin
    export OS_PASSWORD=MXX2VKe067jtD
    export OS_PROJECT_NAME=system
    export OS_DOMAIN_NAME=Default
    export OS_AUTH_URL=http://10.68.22.1:5000/v3
    export OS_REGION_NAME=LocalTest

或aksk认证rc文件:

    export OS_AUTH_URL=http://10.68.22.1:5000/v3
    export OS_ACCESS_KEY=355270364e0a46eb84429e5ffa043842
    export OS_SECRET_KEY=cktuREpGUnVrcjRNeGp0UlZQMmJaRjI4OVQ4UUdLanE=
    export OS_REGION_NAME=LocalTest
    export YUNION_INSECURE=true

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
* requests
* pycrypto>=2.6

首先，需要认证初始化client实例：

可以使用用户名和密码认证

```python
import yunionclient.api.client

desc = {
    'project_name': 'system',
    'project_id': None,
    'args': (
        'https://nn.nnn.nnn.nnn:30357/v3',  # auth_url
        'sysadmin',                         # username
        'pppppppppppppppp',                 # password
        None,                               # domain
    ),
    'kwargs': {
        'region': 'YunionHQ',
        'zone': None,
        'insecure': True,
        'endpoint_type': 'publicURL',
    },
}

args = desc['args']
kwargs = desc['kwargs']
client = yunionclient.api.client.Client(*args, **kwargs)
project_name = desc.get('project_name')
project_id = desc.get('project_id')
if project_name is not None or project_id is not None:
    client.set_project(project_name=project_name, project_id=project_id)
```

也可以使用Access Key/Secret认证：

```python
client = yunionclient.api.client.Client(
    'https://nn.nnn.nnn.nnn:30500/v3',
    region='YunionHQ',
    endpoint_type='publicURL',
    insecure=True,
)
client.authenticate_by_access_key('355270364e0a46eb84429e5ffa043842', 'cktuREpGUnVrcjRNeGp0UlZQMmJaRjI4OVQ4UUdLanE=')
```

Access Key/Secret可以通过climc获取：

```bash
climc credential-create-aksk
```

初始化client之后，则可以调用client的各个资源实例来访问各个资源的API，例如，虚拟机使用client.guests，镜像使用 client.images。

client目前仅支持了部分资源，具体参考 yunionclient/api/client.py 中 client.__init__ 方法的资源的初始化列表。如果您有需要使用的资源未支持的，可以给我们提issue或者自行添加。

一般来说，每个资源实例都实现了下列的一系列方法：

|------------------------|-----------------------------------------------------------|----------------------------------------------------------------------|
| 操作                   | 方法                                                      | 举例                                                                 |
|------------------------|-----------------------------------------------------------|----------------------------------------------------------------------|
| 创建资源               | client.<resources>.create(**kwargs)                       | client.guests.create(**kwargs)                                       |
| 获得资源列表           | client.<resources>.list(**filters)                        | client.guests.list(**{scope=system})                                 |
| 执行资源的操作         | client.<resources>.perform_class_action(action, **kwargs) | client.guests.perform_class_action('validate_create_data', **kwargs) |
| 获取某个资源的详情     | client.<resources>.get(id)                                | client.guests.get(id)                                                |
| 获取某个资源的特定属性 | client.<resources>.get_spec(id, spec)                     | client.guests.get_spec(id, 'vnc')                                    |
| 更新资源的属性         | client.<resources>.update(id, **kwargs)                   | client.guests.update(id, **{name: 'new-name'})                       |
| 执行某个资源的操作     | client.<resources>.perform_action(id, action, **kwargs)   | client.guests.perform_action(id, 'start')                            |
| 删除某个资源           | client.<resources>.delete(id)                             | client.guests.delete(id)                                             |
|------------------------|-----------------------------------------------------------|----------------------------------------------------------------------|

具体方法参数，可以参考API文档：https://www.cloudpods.org/zh/docs/swagger


示例代码
-------------------


```python
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import yunionclient.api.client

#desc = {
#    'project_name': 'system',
#    'project_id': None,
#    'args': (
#        'https://nn.nnn.nnn.nnn:30357/v3',  # auth_url
#        'sysadmin',                         # username
#        'pppppppppppppppp',                 # password
#        None,                               # domain
#    ),
#    'kwargs': {
#        'region': 'YunionHQ',
#        'zone': None,
#        'insecure': True,
#        'endpoint_type': 'publicURL',
#    },
#}
#
#args = desc['args']
#kwargs = desc['kwargs']
#client = yunionclient.api.client.Client(*args, **kwargs)
#project_name = desc.get('project_name')
#project_id = desc.get('project_id')
#if project_name is not None or project_id is not None:
#    client.set_project(project_name=project_name, project_id=project_id)

# 秘钥认证方式
client = yunionclient.api.client.Client(
    'https://nn.nnn.nnn.nnn:30357/v3',
    region='YunionHQ',
    endpoint_type='publicURL',
    insecure=True,
)
client.authenticate_by_access_key('355270364e0a46eb84429e5ffa043842', 'cktuREpGUnVrcjRNeGp0UlZQMmJaRjI4OVQ4UUdLanE=')

# List all public images
imgs, total, limit, offset = client.images.list(is_public='false', status='active')
if len(imgs) == 0:
    raise Exception('No image found')

def waitStatus(guest, xstatus):
	import time
	while True:
		time.sleep(1)
		guest = client.guests.get(guest['id'])
		status = guest['status']
		print('guest status: {}'.format(status))
		if status in xstatus:
			return

# Create a guest server with the 1st image in the list
img_id = imgs[0]['id']
params = {}
params['generate_name'] = 'test' # or params['name'] = 'test'
params['vcpu_count'] = 1
params['vmem_size'] = 64 # memory size 64MB
params['disable_delete'] = False
params['disks'] = [
    {
        'index': 0,
        'image_id': img_id,	# rootfs for operating system
    },
    {
        'index': 1,
        'size': '1024',		# data disk 1024MB
    },
]

# To do batch create, call client.guests.batch_create(3, **params).  When count
# is greater than 1, the returned value will be a list of created guests
guest = client.guests.create(**params)
if isinstance(guest, list) and len(guest) > 0:
    guest = guest[0]['body']
print('guest created:', guest)

print('start guest when it\'s ready')
waitStatus(guest, ['ready'])
client.guests.perform_action(guest['id'], 'start')
waitStatus(guest, ['running'])

print('put it into recycle bin (pending_deleted=True)')
client.guests.delete(guest['id'])
waitStatus(guest, ['ready'])

print('real delete it to actually reclaim resources')
client.guests.delete(guest['id'], override_pending_delete=True)
from yunionclient.common import exceptions
try:
	waitStatus(guest, [])
except exceptions.NotFound:
	print('guest deleted')
```
