# def add(x: int, y: int) -> int:
#
#     """Adds two numbers"""
#     return x + y
#
# # print(add.__name__)
# # print(add.__doc__)
# # print(add.__annotations__)
#
# def operate(x, y, func):
#      return func(x, y)
#
# print(operate(2, 3,add))
#
# def sub(x, y):
#     return y - x
# print(operate(5, 8, sub))
#
# def multiply(a):
#     def by(b):
#         return a * b
#     return by
#
# multiply_by_five = multiply(5)
# print(multiply_by_five(6))


def operate(x, y, func):
    return func(x, y)

add = lambda a, b: a + b
print(add.__name__)
print(add(10, 9))
print(operate(2, 3, add))
print(operate(2, 3, lambda a, b: a+b))
print(operate(2, 3, lambda a, b: b - a))
print(operate(2, 3, lambda w, y: w * y))


import builtins
sum = 67

print(builtins.sum([1, 2, 3]))

print(round(44.655432, 1))

# arr = [1,2,3,4,5]
# print(sum(arr, 100))


fruits = "apple pear cucumber mango grape melon".split()
print(max(fruits, key=len))
print(min(fruits, key=len))
print(max(fruits, key=lambda x: x[-1]))


iterable1 = (1, 2, 3, 4)
iterable2 = ('hello', 'how', 'are', 'you')
print(dict(zip(iterable2, iterable1)))
print(list(zip(iterable2, iterable1, strict=True)))
print(sorted('helloAZ', reverse=True))
print(sorted(fruits, key=lambda x: x[-1]))

lst = [1, 2, 3, 4, 5]
print(list(map(lambda x: x**2, lst)))
print([x**2 for x in lst])
print(list(map(lambda x: x.upper(), fruits)))
fruits.append('Agbado')
print(list(filter(str.istitle, fruits)))
print(list(filter(lambda x: not x.istitle(), fruits)))
print([x for x in fruits if not x.istitle()])
