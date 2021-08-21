Cloudpods Python 3 SDK
======================

本仓库提供了访问Cloudpods API的Python 3 SDK以及基于该SDK的climc客户端代码。


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

```python
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

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

# List all public images
imgs, total, limit, offset = client.images.list(is_public='false')
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
params['name'] = 'test'
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
