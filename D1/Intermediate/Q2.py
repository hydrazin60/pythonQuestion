## Create a program to check if a number is prime using a loop.
number = int(input("Enter a number to check prime or not : "))
i = 2
isPrime = False
while i <=9:
    if number % i == 0 and number !=i:
        isPrime =  True
        break
    i +=1

if isPrime:
     print(f"{number} is not a prime number.")
else:
    print(f"{number} is  a prime number.")    



#  for loop
number = int(input("Enter a number to check prime or not: "))
isPrime = False  
for i in range(2, 10):
    if number % i == 0 and number != i:   
        break
if isPrime:
    print(f"{number} is not a prime number.")
else:
    print(f"{number} is a prime number.")
