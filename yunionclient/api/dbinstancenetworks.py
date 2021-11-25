import yunionclient

from yunionclient.common import base


class DBInstancenetworkManager(base.JointManager):
    keyword = 'dbinstancenetwork'
    keyword_plural = 'dbinstancenetworks'
    _columns = ['Dbinstance_Id', 'Dbinstance', 'Network_ID', 'Network', 'IP_addr']

    @classmethod
    def master_class(cls):
        return yunionclient.api.dbinstances.DbinstanceManager

    @classmethod
    def slave_class(cls):
        return yunionclient.api.networks.NetworkManager
