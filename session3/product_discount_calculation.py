import collections


def product_parameters_food(product_index):
    return product_index/(product_index+100), product_index/(product_index+300)


def product_parameters_beverage(product_index):
    return product_index/(product_index+300), product_index/(product_index+400)


def product_parameters_raw_material(product_index):
    return product_index/(product_index+400), product_index/(product_index+700)


def calculate_discount(parameter_func, order):
    param_index = parameter_func(order.product_index)
    return param_index[0]*order.quantity + param_index[1]*order.price


def main():
    # using namedtuple from collections package to illustrate Order object, of course you can use class or dataclass
    Order = collections.namedtuple('Order', ['id', 'product_index', 'quantity', 'price', 'discount'])
    order = Order(10, 100, 20, 4, 0.0)

    product_type = "Food"
    param_func = (product_parameters_food if product_type == 'Food'
                  else (product_parameters_beverage if product_type == 'Beverage'
                        else product_parameters_raw_material))

    order_discount = calculate_discount(param_func, order)
    print(order_discount)


if __name__ == '__main__':
    main()
