from functools import reduce


def composite(*func):
    def compose(f, g):
        return lambda x: f(g(x))

    return reduce(compose, func, lambda x: x)
