def example(a, b, **kw):
    return a * b


if __name__ == '__main__':
    print(type(example))
    print(example.__code__.co_varnames)
    print(example.__code__.co_argcount)
    print(example.__code__.co_freevars)
    print(example.__code__.co_consts)
