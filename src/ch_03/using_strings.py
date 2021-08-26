from decimal import *
from typing import Text, Optional


def clean_decimal(text: Text) -> Optional[Text]:
    if text is None:
        return None
    return Decimal(text.replace('$', '').replace(',', ''))


def replace(str: Text, a: Text, b: Text) -> Text:
    return str.replace(a, b)


def remove(str: Text, chars: Text) -> Text:
    if chars:
        return remove(str.replace(chars[0], ''), chars[1:])
    return str


if __name__ == '__main__':
    cd = remove('text$%,', '$,%')
    print(cd)
