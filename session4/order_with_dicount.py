from functional import seq
from order_rules import OrderRule
from dataclasses import dataclass


# Define Order as dataclass
@dataclass
class Order:
    id: int
    product_index: int
    quantity: int
    price: int
    discount: float = 0.0


def get_order_with_discount(order, rules):
    discount = (seq(rules)
                .where(lambda rule: rule.qualify(order))
                .select(lambda rule: rule.discount(order))
                .order_by(lambda x: x)[:2]
                .average())

    order.discount = round(discount, 2)
    return order


def main():
    orders = [Order(2, 200, 10, 5, 0.0), Order(3, 300, 20, 10, 0.0), Order(4, 400, 30, 15, 0.0),
              Order(5, 500, 40, 20, 0.0), Order(6, 600, 50, 25, 0.0)]

    orders_with_discount = seq(orders).map(lambda order: get_order_with_discount(order, OrderRule.rules())).to_list()

    print(orders_with_discount)


if __name__ == '__main__':
    main()
