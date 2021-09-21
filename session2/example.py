from functional import seq


def add_one(x):
    return x + 1


def square(x):
    return x**2


def subtract_10(x):
    return x - 10


# Python does not support natively functional method chaining,
# I use very good external package that add this to Python:: https://github.com/EntilZha/PyFunctional
my_data = seq([7, 4, 5, 6, 3, 8, 10])

# 1st example
result1 = my_data.map(add_one).map(square).map(subtract_10).for_each(print)
print('-'*10)

# 2nd example
result2 = my_data.map(add_one).map(square).filter(lambda x: x < 20).map(subtract_10).for_each(print)
print('-'*10)

# 3rd example
# using list slicing to return first 2 elements [:2]
result3 = my_data.map(add_one).map(square).filter(lambda x: x < 70).sorted()[:2].map(subtract_10).for_each(print)
print('-'*10)
