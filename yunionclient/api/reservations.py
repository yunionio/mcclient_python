from yunionclient.common import base

class Reservation(base.ResourceBase):
    pass


class ReservationManager(base.MeterManager):
    resource_class = Reservation
    keyword = 'reservation'
    keyword_plural = 'reservations'
    _columns = ["cloudaccount_id","resource_type","reservation_years","lookback_days","payment_option","offering_class","category","spec","instance_amount","monthly_savings_amount","upfront_cost","average_utilization","monthly_cost","total_savings_amount","total_savings_percentage","currency","details"]