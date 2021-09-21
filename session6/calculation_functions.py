from models import Invoice, Shipping, Freight, Availability, ShippingDate
from datetime import timedelta


def calc_invoice_1(order):
    print('calc_invoice_1 ...')
    return Invoice(order.cost * 1.1)


def calc_invoice_2(order):
    print('calc_invoice_2 ...')
    return Invoice(order.cost * 1.2)


def calc_invoice_3(order):
    print('calc_invoice_3 ...')
    return Invoice(order.cost * 1.3)


def calc_invoice_4(order):
    print('calc_invoice_4 ...')
    return Invoice(order.cost * 1.4)


def calc_invoice_5(order):
    print('calc_invoice_5 ...')
    return Invoice(order.cost * 1.5)


def calc_shipping_1(invoice):
    print('calc_shipping_1 ...')
    shipping_id = 1 if invoice.cost > 1000 else 2
    return Shipping(id=shipping_id, cost=invoice.cost)


def calc_shipping_2(invoice):
    print('calc_shipping_2 ...')
    shipping_id = 1 if invoice.cost > 1100 else 2
    return Shipping(id=shipping_id, cost=invoice.cost)


def calc_shipping_3(invoice):
    print('calc_shipping_3 ...')
    shipping_id = 1 if invoice.cost > 1200 else 2
    return Shipping(id=shipping_id, cost=invoice.cost)


def calc_freight_cost_1(shipping):
    print('calc_freight_cost_1 ...')
    freight_cost = shipping.cost * 0.25 if shipping.id == 1 else shipping.cost * 0.5
    return Freight(freight_cost)


def calc_freight_cost_2(shipping):
    print('calc_freight_cost_2 ...')
    freight_cost = shipping.cost * 0.28 if shipping.id == 1 else shipping.cost * 0.52
    return Freight(freight_cost)


def calc_freight_cost_3(shipping):
    print('calc_freight_cost_3 ...')
    freight_cost = shipping.cost * 0.3 if shipping.id == 1 else shipping.cost * 0.6
    return Freight(freight_cost)


def calc_freight_cost_4(shipping):
    print('calc_freight_cost_4 ...')
    freight_cost = shipping.cost * 0.35 if shipping.id == 1 else shipping.cost * 0.65
    return Freight(freight_cost)


def calc_freight_cost_5(shipping):
    print('calc_freight_cost_5 ...')
    freight_cost = shipping.cost * 0.15 if shipping.id == 1 else shipping.cost * 0.2
    return Freight(freight_cost)


def calc_freight_cost_6(shipping):
    print('calc_freight_cost_6 ...')
    freight_cost = shipping.cost * 0.1 if shipping.id == 1 else shipping.cost * 0.15
    return Freight(freight_cost)


def calc_availability_1(order):
    print('calc_availability_1 ...')
    availability_date = order.date + timedelta(days=3)
    return Availability(availability_date)


def calc_availability_2(order):
    print('calc_availability_2 ...')
    availability_date = order.date + timedelta(days=2)
    return Availability(availability_date)


def calc_availability_3(order):
    print('calc_availability_3 ...')
    availability_date = order.date + timedelta(days=1)
    return Availability(availability_date)


def calc_availability_4(order):
    print('calc_availability_4 ...')
    availability_date = order.date + timedelta(days=4)
    return Availability(availability_date)


def calc_shipping_date_1(availability):
    print('calc_shipping_date_1 ...')
    shipping_date = availability.date + timedelta(days=1)
    return ShippingDate(shipping_date)


def calc_shipping_date_2(availability):
    print('calc_shipping_date_2 ...')
    shipping_date = availability.date + timedelta(days=2)
    return ShippingDate(shipping_date)


def calc_shipping_date_3(availability):
    print('calc_shipping_date_3 ...')
    shipping_date = availability.date + timedelta(hours=14)
    return ShippingDate(shipping_date)


def calc_shipping_date_4(availability):
    print('calc_shipping_date_4 ...')
    shipping_date = availability.date + timedelta(hours=20)
    return ShippingDate(shipping_date)


def calc_shipping_date_5(availability):
    print('calc_shipping_date_5 ...')
    shipping_date = availability.date + timedelta(hours=10)
    return ShippingDate(shipping_date)


