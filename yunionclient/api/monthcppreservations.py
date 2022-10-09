from yunionclient.common import base

class MonthCppReservation(base.ResourceBase):
    pass


class MonthCppReservationManager(base.MeterManager):
    resource_class = MonthCppReservation
    keyword = 'month_cpp_reservation'
    keyword_plural = 'month_cpp_reservations'
    _columns = ["cloudaccount_id","reservation_id","reservation_years","lookback_days","payment_option","offering_class","category","spec","instance_amount","monthly_savings_amount","upfront_cost","average_utilization","monthly_cost","total_savings_amount","total_savings_percentage","currency","details","cpp_count","cpp_rate"]