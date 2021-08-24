m = list()

for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        m.append(n)


# summable list
class SummableList(list):
    def sum(self):
        s = 0
        for v in self:
            s += v
        return s


if __name__ == '__main__':
    print(sum(m))
    print('**' * 5)
    print('Summable List')
    m = SummableList(range(1, 10))
    print(m.sum())
