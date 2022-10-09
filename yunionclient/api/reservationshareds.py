from yunionclient.common import base

class ReservationShared(base.ResourceBase):
    pass


class ReservationSharedManager(base.MeterManager):
    resource_class = ReservationShared
    keyword = 'reservation_shared'
    keyword_plural = 'reservation_shareds'
    _columns = ["cloudaccount_id","reservation_id","reservation_years","lookback_days","payment_option","offering_class","category","spec","instance_amount","monthly_savings_amount","upfront_cost","average_utilization","monthly_cost","total_savings_amount","total_savings_percentage","currency","details","cpp_count","cpp_rate"]