# generator expressions
import math
from collections import Iterator


def pfactors(x: int) -> Iterator[int]:
    if x % 2 == 0:
        yield 2

        if x // 2 > 1:
            yield from pfactors(x // 2)
        return
    for i in range(3, int(math.sqrt(x) + .5) + 1, 2):
        if x % i == 0:
            yield i

            if x // i > 1:
                yield from pfactors(x // i)
            return
    yield x


def pfactorsr(x: int) -> Iterator[int]:
    def factor_n(x: int, n: int) -> Iterator[int]:
        if n * n > x:
            yield x
            return
        if x % n == 0:
            yield n
            if x // n > 1:
                yield from factor_n(x // n, n)
        else:
            yield from factor_n(x, n + 2)
    if x % 2 == 0:
        yield 2
        if x // 2 > 1:
            yield from pfactorsr(x // 2)
        return
    yield from factor_n(x, 3)
