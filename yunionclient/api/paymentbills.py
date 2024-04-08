from yunionclient.common import base

class PaymentBill(base.ResourceBase):
    pass


class PaymentBillManager(base.MeterManager):
    resource_class = PaymentBill
    keyword = 'payment_bill'
    keyword_plural = 'payment_bills'
    _columns = ["account", "account_id", "charge_type", "region", "region_id", "domain", "domain_id", "project",
                "tenant_id", "brand", "resource_id", "resource_type", "resource_name", "rate", "reserved", "spec",
                "usage_type", "associate_id", "day", "price_unit", "currency", "cloudprovider_id", "cloudprovider_name",
                "amount", "gross_amount", "usage"]
