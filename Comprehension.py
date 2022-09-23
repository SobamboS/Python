# List Comprehension

# cont = []
# for i in range(1, 11):
#     cont.append(i)
# print(cont)

# or you can do it like this
# cont = [ i for i in range (1, 11)]
# print(cont)
# count = [num**2 for num in range(1, 11)]
# print(count)


 # to find the square
# squares = []
# for i in range(1, 11):
#     squares.append(i ** 2)
# print(squares)



# to find the names starting with capital letter
# names = ['bimpe', 'Banke', 'abimbola', 'James', 'olalekan', 'Rachael', 'Kelelchi']
# my_names = [name for name in names if name.istitle()]
# number_of_items = int(input("How many names will you like to enter ? "))
# input_names = [input(f"{i+1}.Name? ")for i in range(number_of_items)]
# my_names = []
# print(input_names)



# my_names = []
# for name in names:
#     if name.istitle():
#         my_names.append(name)
# print(my_names)

# evens = [even for even in range (1, 11) if even %  2 ==0]
# even_square_odd_cube = [num**2 if num % 2 == 0 else num **3 for num in range (1, 11)]
# print(evens)
# print(even_square_odd_cube)
#
#
# x_and_y = []
# for x in range(1, 5):
#     for y in range(1, 5):
#         x_and_y.append((x, y))
#         print(x_and_y)
#
# x_and_y = [(x, y) for x in range(1, 6) for y in range(1, 6)]
# print(x_and_y)


listcomp = [num % 3 for num in range (1, 10)]
setcomp = {num % 3 for num in range (1, 10)}
dictcomp = {k: v for k, v in enumerate(range(11, 16))}
genexp = (num for num in range(1, 6))

print(type(listcomp), listcomp)
print(type(setcomp), setcomp)
print(type(dictcomp), dictcomp)
print(type(genexp), genexp)

print(next(genexp))
print(list(genexp))