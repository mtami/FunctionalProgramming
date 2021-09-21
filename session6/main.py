from availability_path import AvailabilityPath
from invoicing_path import InvoicingPath
from utils import composite
from functional import seq
from functools import partial
from models import (ProcessConfiguration, InvoiceChoice, ShippingChoice,
                    FreightChoice, AvailabilityChoice, ShippingDateChoice, Customer, Order)
from datetime import datetime
from typing import Type


def set_configurations():
    customer = Customer('Tami3')
    order = Order(customer=customer, date=datetime.today(), cost=2100)
    process_config = ProcessConfiguration(invoice_choice=InvoiceChoice.inv3,
                                          shipping_choice=ShippingChoice.ship1,
                                          freight_choice=FreightChoice.fr6,
                                          availability_choice=AvailabilityChoice.av2,
                                          shipping_date_choice=ShippingDateChoice.sd1)
    return order, process_config


def availability_path_func(config: ProcessConfiguration, availability_path: Type[AvailabilityPath]):
    func_1 = (seq(availability_path.availability_funcs())
              .where(lambda x: x[0] == config.availability_choice)
              .select(lambda x: x[1]).first())
    func_2 = (seq(availability_path.shipping_date_funcs())
              .where(lambda x: x[0] == config.shipping_date_choice)
              .select(lambda x: x[1]).first())

    return composite(func_2, func_1)


def invoice_path_func(config: ProcessConfiguration, invoice_path: Type[InvoicingPath]):
    func_1 = (seq(invoice_path.invoice_funcs())
              .where(lambda x: x[0] == config.invoice_choice)
              .select(lambda x: x[1]).first())

    func_2 = (seq(invoice_path.shipping_funcs())
              .where(lambda x: x[0] == config.shipping_choice)
              .select(lambda x: x[1]).first())

    func_3 = (seq(invoice_path.freight_funcs())
              .where(lambda x: x[0] == config.freight_choice)
              .select(lambda x: x[1]).first())

    return composite(func_3, func_2, func_1)


def adjust_cost(order, order_freight_func, order_shipping_date_func):
    freight = order_freight_func(order)
    shipping_date = order_shipping_date_func(order)

    print("Day of Shipping : ", shipping_date.date.strftime("%A"))
    # 0 is Monday
    cost = freight.cost + 1000 if shipping_date.date.weekday() == 0 else freight.cost + 500
    return cost


def main():
    order, config = set_configurations()
    cost_of_order = partial(adjust_cost, order_freight_func=invoice_path_func(config, InvoicingPath),
                            order_shipping_date_func=availability_path_func(config, AvailabilityPath))

    print(cost_of_order(order))


if __name__ == '__main__':
    main()
