## Write a program to find the factorial of a given number using a loop.
n = int(input("enter a number which you want to find factorial ")) 
i = 1
factorial = 1
while i <= n:
    factorial = factorial*i
    i +=1
print(f"The factorial of {n} is: {factorial}")    
    