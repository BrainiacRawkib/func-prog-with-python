# higher order functions: passing a function as an arg

year_cheese = [
    (2000, 29.87), (2001, 30.12), (2002, 30.6), (2003, 30.66), (2004, 31.33),
    (2005, 32.62), (2006, 32.73), (2007, 33.5), (2008, 32.84), (2009, 33.02),
    (2010, 32.92)
]


# fst and snd()
snd = lambda x: x[1]

if __name__ == "__main__":
    print(max(year_cheese))  # uses the first item to locate the largest value
    print(max(year_cheese, key=lambda yc: yc[1]))  # uses the second item to locate the largest value
    print('*' * 10 + "wrap-process-unwrap pattern" + '*' * 10)
    print(max(map(lambda yc: (yc[1], yc), year_cheese))[1])
    print('*' * 10 + "fst and snd" + '*' * 10)
    print(snd(max(map(lambda yc: (yc[1], yc), year_cheese))))
