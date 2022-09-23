number = 8
Factorial = 1

if  number == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        Factorial = Factorial * i
    print("The factorial of is", Factorial)
