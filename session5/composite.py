from functional import seq
from functools import reduce


def add_one(x):
    return x + 1


def square(x):
    return x**2


def subtract_10(x):
    return x - 10


def composite_func(f1, f2, f3):
    return lambda x: f1(f2(f3(x)))


# composite_function accepts N
# number of function as an
# argument and then compose them
def super_composite_function(*func):
    def compose(f, g):
        return lambda x: f(g(x))

    return reduce(compose, func, lambda x: x)


def main():
    my_data = seq([3, 5, 7, 8])

    # 1st example
    my_data.map(add_one).map(square).map(subtract_10).for_each(print)
    print('-'*10)

    # 2nd example
    my_data.map(lambda x: subtract_10(square(add_one(x)))).for_each(print)
    print('-'*10)

    # 3rd example
    my_composite_func = composite_func(subtract_10, square, add_one)
    my_data.map(my_composite_func).for_each(print)
    print('-'*10)

    # extra example using python *non-keywords argument* feature
    my_super_composite_func = super_composite_function(subtract_10, square, add_one)
    my_data.map(my_super_composite_func).for_each(print)
    print('-'*10)

    add_one_square = super_composite_function(add_one, square)
    add_one_square_subtract_10 = super_composite_function(add_one_square, subtract_10)
    my_data.map(add_one_square_subtract_10).for_each(print)
    print('-'*10)


if __name__ == '__main__':
    main()