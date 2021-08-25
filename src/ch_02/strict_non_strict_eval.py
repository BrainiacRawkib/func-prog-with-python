def numbers():
    for i in range(1024):
        print(f'= {i}')
        yield i


def sum_to(n: int) -> int:
    sum_: int = 0
    for i in numbers():
        if i == n:
            break
        sum_ += i
    return sum_


if __name__ == '__main__':
    print(sum_to(5))
