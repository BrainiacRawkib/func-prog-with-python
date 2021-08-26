from typing import Tuple, Callable, NamedTuple
from collections import namedtuple


RGB = Tuple[int, int, int]
red: Callable[[RGB], int] = lambda color: color[0]


color = namedtuple('Color', ('red', 'green', 'blue', 'name'))


class Color(NamedTuple):
    """An RGB color."""
    red: int
    green: int
    blue: int
    name: str


if __name__ == '__main__':
    print(color.red)
