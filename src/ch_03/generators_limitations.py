from generator_expressions import pfactors


if __name__ == '__main__':
    factors = pfactors(1560)
    print(sum(factors))
