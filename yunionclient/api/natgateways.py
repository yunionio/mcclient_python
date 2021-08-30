from yunionclient.common import base

class Natgateway(base.ResourceBase):
    pass


class NatgatewayManager(base.StandaloneManager):
    resource_class = Natgateway
    keyword = 'natgateway'
    keyword_plural = 'natgateways'
    _columns = ["ID", "Name", "Enabled",
                "Status", "Cloudregion_Id", "Region", "Vpc_Id", "Charge_Type", "Nat_Spec",
                ]
    _admin_columns = []
