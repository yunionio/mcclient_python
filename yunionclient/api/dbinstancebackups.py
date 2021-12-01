from yunionclient.common import base

class Dbinstancebackup(base.ResourceBase):
    pass


class DbinstancebackupManager(base.StandaloneManager):
    resource_class = Dbinstancebackup
    keyword = 'dbinstancebackup'
    keyword_plural = 'dbinstancebackups'
    _columns = ["Id", "Name", "Start_Time", "End_Time", "Status", "Backup_Type", "Dbnames", "Backup_Size_Mb", "Dbinstance", "Engine", "Engineversion"]

