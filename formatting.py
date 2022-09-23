import math

s = "Sorry is this {} minute {} ?" .format(5, "Argument")

print("{:^10} is  {:2%} years old ".format("Bill", math.pi * 100))
print(s)

for i in range (1, 11):
    sym = '*' * i
  #  print('{:10}'.format(sym))
    print(f'{sym:>10}')