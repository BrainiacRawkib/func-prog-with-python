from typing import Tuple, Iterable, Iterator, List, Text, cast
from raw_clean_data import head_split_fixed, row_iter


Pair = Tuple[str, str]


def series(n: int, row_iter: Iterable[List[Text]]) -> Iterator[Pair]:
    for row in row_iter:
        yield cast(Pair, tuple(row[n * 2: n * 2 + 2]))


if __name__ == '__main__':
    with open('anscombe.txt') as source:
        data = tuple(head_split_fixed(row_iter(source)))
        sample_I = tuple(series(0, data))
        sample_II = tuple(series(1, data))
        sample_III = tuple(series(2, data))
        sample_IV = tuple(series(3, data))
        print(sample_I)
