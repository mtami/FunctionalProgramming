from models import AvailabilityChoice, ShippingDateChoice
from calculation_functions import (calc_availability_1, calc_availability_2,
                                    calc_availability_3, calc_availability_4,
                                    calc_shipping_date_1, calc_shipping_date_2,
                                    calc_shipping_date_3, calc_shipping_date_4,
                                    calc_shipping_date_5)


class AvailabilityPath:

    @staticmethod
    def availability_funcs():
        return [
            (AvailabilityChoice.av1, calc_availability_1),
            (AvailabilityChoice.av2, calc_availability_2),
            (AvailabilityChoice.av3, calc_availability_3),
            (AvailabilityChoice.av4, calc_availability_4)
        ]

    @staticmethod
    def shipping_date_funcs():
        return [
            (ShippingDateChoice.sd1, calc_shipping_date_1),
            (ShippingDateChoice.sd2, calc_shipping_date_2),
            (ShippingDateChoice.sd3, calc_shipping_date_3),
            (ShippingDateChoice.sd4, calc_shipping_date_4),
            (ShippingDateChoice.sd5, calc_shipping_date_5)
        ]
