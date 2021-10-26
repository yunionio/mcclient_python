from yunionclient.common import base
from yunionclient.common import utils

"""
价格查询接口
"""
class PriceManager(base.MeterManager):
    keyword = 'price'
    keyword_plural = 'prices'
    _columns = []

    '''
    输入参数：
    provider // 云厂商
    region // 区域ID example: cn-north-1
    zone // 可用区ID example: cn-north-1a
    period // 计费时长 default:"1"`
    price_unit // 计费周期 choices: hour (小时) | month (按月) | year (按年) default:"hour"`
    cloud_account // 云账号ID, 用于获取云账号折扣信息
    items  // 查询的资源项列表
    
    注：查询的资源结构
    item = 
    {
        resource_type // 资源类型
        resource_key // 资源规格SKU
        amount // 数量
    }

    响应:
    {
	"price": {
		"currency": "CNY", // 货币单位
		"discount": 1, // 折扣
		"discount_price": 0.237524, // 折扣价
		"original_price": 0.237524, // 原价
        "details": [{
			"amount": 2,   // 资源数量
			"currency": "CNY",  // 货币单位
			"discount": 1, // 折扣
			"discount_price": 0.133334, // 折扣价
			"original_price": 0.133334, // 原价
			"resource_type": "cpu", // 资源类型
			"unit": "1core"  // 资源计量单位
		}, {
			"amount": 2,
			"currency": "CNY",
			"discount": 1,
			"discount_price": 0.06669,
			"original_price": 0.06669,
			"resource_type": "mem",
			"unit": "1GB"
		}, {
			"amount": 30,
			"currency": "CNY",
			"discount": 1,
			"discount_price": 0.0375,
			"original_price": 0.0375,
			"resource_key": "rotate::local",  // 资源规格SKU
			"resource_type": "disk",
			"unit": "1GB"
		}]
	}
}


    例:
    [IDC价格查询]
    items = [{'resource_type': 'cpu', 'amount': 2}, {'resource_type': 'mem', 'amount': 2}, {'resource_type': 'disk', 'resource_key': 'rotate::local', 'amount': 30}]
    self.get_price('OneCloud', '', '', '', items)

    [私有云价格查询]
    items = [
        {'resource_type': 'cpu', 'amount': 2},
        {'resource_type': 'mem', 'amount': 2},
        {'resource_type': 'disk', 'resource_key': 'rotate::rbd', 'amount': 30}]
    self.get_price('OpenStack', '', '', '', items)

    [公有云价格查询]
    // aliyun金融云
    items = [
        {'resource_type': 'instance', 'resource_key': 'ecs.hfc6.large', 'amount': 1},
        {'resource_type': 'disk', 'resource_key': 'cloud_efficiency', 'amount': 30},
        {'resource_type': 'disk', 'resource_key': 'cloud_efficiency', 'amount': 20}]
    self.get_price('Aliyun-fin', 'cn-shenzhen-finance-1', 'cn-shenzhen-finance-1d', '', items)

    // 华为云
    items = [
    {'resource_type': 'instance', 'resource_key': 't6.large.1', 'amount': 1},
    {'resource_type': 'disk', 'resource_key': 'GPSSD', 'amount': 40},
    {'resource_type': 'disk', 'resource_key': 'SAS', 'amount': 20},
    {'resource_type': 'eip', 'resource_key': '5_bgp', 'amount': 10}]
    self.get_price('Huawei', 'cn-east-3', 'cn-east-3c', '', items)
    '''
    def get_price(self, provider, region, zone, cloud_account, items, period='1', price_unit='hour'):
        params = {
          'provider': provider,
          'region': region,
          'zone': zone,
          'cloud_account': cloud_account,
          'period': period,
          'price_unit': price_unit
        }

        for idx, item in enumerate(items):
            for k in item.keys():
                params[f'items.{idx}.{k}'] = item[k]

        url = r'/prices/total?' + utils.urlencode(params)
        return self._get(url, self.keyword)

'''
价格元数据查询
价格元数据主要作用是在不知道具体价格查询参数时，获取系统中支持查询价格的资源参数信息。
价格查询元数据主要包括： 
provider （云厂商）
region    (区域)
zone     （可用区）
resource_type (资源类型)
resource_key  (资源值/资源sku)

例：
1. 查询所有支持价格查询的云厂商
self.price_meta('provider')


2. 查询阿里云所有支持价格查询的资源类型
self.price_meta('resource_type', provider='aliyun')

3. 查询所有支持阿里云主机价格查询的可用区
self.price_meta('zone', provider='aliyun', resource_type='instance')
'''
class PriceMetadataManager(base.MeterManager):
    keyword = 'price_metadata'
    keyword_plural = 'price_metadatas'
    _columns = []

    '''
    输入参数：
    meta // 待查询元数据名称（*必须） choices: provider|region|zone|resource_type|resource_key

    支持的kwargs:
    provider  // 云厂商
    region    // 区域ID, example: cn-north-1
    zone      // 可用区ID example: cn-north-1a
    resource_type // 资源类型
    '''
    def price_meta(self, meta, **kwargs):
        kwargs['meta'] = meta
        url = r'/price_metadatas?' + utils.urlencode(kwargs)
        return self._get(url, self.keyword_plural)