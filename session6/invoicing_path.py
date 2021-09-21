from models import InvoiceChoice, ShippingChoice, FreightChoice
from calculation_functions import (calc_invoice_1, calc_invoice_2,
                                   calc_invoice_3, calc_invoice_4, calc_invoice_5,
                                   calc_shipping_1, calc_shipping_2, calc_shipping_3,
                                   calc_freight_cost_1, calc_freight_cost_2, calc_freight_cost_3,
                                   calc_freight_cost_4, calc_freight_cost_5, calc_freight_cost_6)


class InvoicingPath:

    @staticmethod
    def invoice_funcs():
        return [
            (InvoiceChoice.inv1, calc_invoice_1),
            (InvoiceChoice.inv2, calc_invoice_2),
            (InvoiceChoice.inv3, calc_invoice_3),
            (InvoiceChoice.inv4, calc_invoice_4),
            (InvoiceChoice.inv5, calc_invoice_5)
        ]

    @staticmethod
    def shipping_funcs():
        return [
            (ShippingChoice.ship1, calc_shipping_1),
            (ShippingChoice.ship2, calc_shipping_2),
            (ShippingChoice.ship3, calc_shipping_3)
        ]

    @staticmethod
    def freight_funcs():
        return [
            (FreightChoice.fr1, calc_freight_cost_1),
            (FreightChoice.fr2, calc_freight_cost_2),
            (FreightChoice.fr3, calc_freight_cost_3),
            (FreightChoice.fr4, calc_freight_cost_4),
            (FreightChoice.fr5, calc_freight_cost_5),
            (FreightChoice.fr6, calc_freight_cost_6)
        ]
