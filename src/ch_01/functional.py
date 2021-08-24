s = 0
for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        s += n


# sum of a sequence (recursive)
def sumr(seq):
    if len(seq) == 0:
        return 0
    return seq[0] + sumr(seq[1:])


# sequence of values
def until(n, filter_func, v):
    if v == n:
        return []
    if filter_func(v):
        return [v] + until(n, filter_func, v + 1)
    else:
        return until(n, filter_func, v + 1)


# newton-raphson algorithm
def next_(n, x):
    return (x + n / x) / 2


n = 2
f = lambda x: next_(n, x)
a0 = 1.0
res = [round(x, 4) for x in (a0, f(a0), f(f(a0)), f(f(f(a0))),)]

if __name__ == '__main__':
    print(s)
    print('*' * 10 + "Sum of a sequence using recursion" + '*' * 10)
    print(sumr([7, 11]))
    print(7 + sumr([11]))
    print(sumr([7, 11, 12]))
    print(18 + sumr([7, 11, 12]))
    print(18 + sumr([]))
    print('*' * 10 + "generating multiples of 3 and 5 using recursion" + '*' * 10)
    i = until(10, lambda x: x % 3 == 0 or x % 5 == 0, 0)
    print(i)
    print('*' * 10 + "newton-raphson algorithm" + '*' * 10)
    print(res)
