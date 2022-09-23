number: int = int(intput("Enter a number : "))

fact: int = 1
total: int = 0
while fact < number:
 if  number % fact == 0:
     total += fact
     fact += 1
 if  total == number:
     print(number, "is a perfect number")
elif total > number:
     print(number, "is abundant")
else:
     print(number, "is deficient")
