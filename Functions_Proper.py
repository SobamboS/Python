def funct(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)
funct(1, 2, 3, 4, 5, 6)


def func(**kwargs):
    print(kwargs)
func(a=1, b=2, c=3, d=4, e=5)


