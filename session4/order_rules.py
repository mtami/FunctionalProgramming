from collections import namedtuple

_OrderRule = namedtuple('Rule', 'qualify discount')


class OrderRule:

    @staticmethod
    def rules():
        return [
            _OrderRule(OrderRule.qualify_order_id, OrderRule.calculate_order_id_discount),
            _OrderRule(OrderRule.qualify_price, OrderRule.calculate_price_discount),
            _OrderRule(OrderRule.qualify_quantity, OrderRule.calculate_quantity_discount)
        ]

    @staticmethod
    def qualify_price(order):
        return order.price > 20

    @staticmethod
    def calculate_price_discount(order):
        return order.price / 2

    @staticmethod
    def qualify_quantity(order):
        return order.quantity > 20

    @staticmethod
    def calculate_quantity_discount(order):
        return order.price / 3

    @staticmethod
    def qualify_order_id(order):
        return order.id > 1

    @staticmethod
    def calculate_order_id_discount(order):
        return order.price / 10

# from dataclasses import dataclass
#
#
# # Define Order as dataclass
# @dataclass
# class Order:
#     id: int
#     product_index: int
#     quantity: int
#     price: int
#     discount: float = 0.0
#
# order = Order(1, 100, 10, 5, 0.0)
# from functional import seq
# seq([OrderRule.rules]).where(lambda rule: rule[0](order))