from functools import reduce
from math import prod

lst = [1, 2, 3, 4, 5]

def reduce_func(acc, item):
    print(f"acc -> {acc} <> item -> {item}")
    return acc + item

print("\n############ Reduce ############\n")
print(reduce(lambda acc, item: acc + item, lst))
print(lst)
print(reduce(reduce_func, lst, 100))
# print(reduce(lst, 100))
print(sum(lst, 100))
print(prod(lst, start=100))
print(reduce(lambda acc, item: acc if acc > item else item, lst))
print(max(lst))


print("\n########### match ############\n")

number = int(input('Enter a number'))

match number:
    case 1:
        print(1)

    case 2:
        print(2)

    case _:
        print("Don't fucking know you")

number = int(input('Enter a number'))

match number:
    case _ as x if 1 <= x <= 10:
        print(x)
    case _ as x if 11 <= x <= 20:
        print(x)
    case _:
        print("Don't fucking know you")


print("\n############ Match a list########################\n")

lst = [20, 13, 16]
lst = [20, [13, 5],'good']

match lst:

    case[x, y, int(z)]:
        print(x, z, y)

    case [a,[b,c], d]:
        print(a, b, c, d)

    case _:
        print('Nothing matched')



d ={
    'name': 'Pearson',
    'age': 18,
    'is_swit': True
}

match d:
    case{'name': str(name), 'age': int(age)}:
        print(name, age)

    case _:
        print('Nothing to match''')


print("\n########################## switch with a function#############\n")


def fizzbuzz(num):
    three = num % 3
    five = num % 5
    match(three, five):
         case(0, 0):
          return "fizzbuzz"
         case(0, _):
             return "fizz"
         case(_, 0):
             return "Buzz"
         case _:
             return num

for i in range(1, 101):
    print(fizzbuzz(i))



def summing_list(list_: list[int]) -> int | None:
    match list_:
        case[]:
            return 0
        case [first_value, *another_list]:
            return first_value + summing_list(another_list)
        case _:
            print("Can only accept an int")
            return None

print(summing_list([1, 2, 3, 4, 5]))

print("\n################ Using Zip ###########\n")

import itertools
print(summing_list(([1, 2, 3, 4, 5])))
print(list(itertools.zip_longest([1, 2], [3, 4, 5], fillvalue=0)))

print(globals())

def func(num):
    print(locals())

    func(15)


a = 5
def func1():
#a = 7
 print(a)

func1()

a+=8

func1()

a = 6

def funct():
    b = 10

    def innner_funct():
        nonlocal b
        b += 2

        print(b)
    inner_funct()
    print(b)

funct()
