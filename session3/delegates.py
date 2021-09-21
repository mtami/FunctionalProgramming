# python support high order function without the need to define delegate variable
# This possible because everything in Python (>3) is an object even a function
# In other words, functions in Python are first-class citizens

def test1(x):
    return x/2


def test2(x):
    return x/4 + 1


# Higher Order Function
def test(func, v):
    return func(v) + v


fun_list = [test1, test2]

# you can assign function to variable -> delegate
# test_x = test
# print(test_x(6))


# Using simple Calling methods
print(test2(test1(5.0)))
print(test1(test2(5.0)))

# Using the function from the list
print(fun_list[0](5.0))
print(fun_list[1](5.0))

# Using The Higher Order Function
print(test(test1, 5.0))
print(test(test2, 5.0))
