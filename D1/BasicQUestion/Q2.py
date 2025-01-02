# # Write a program to calculate the sum of all even numbers from 1 to 10.
i = 0
sum = 0
while i < 10:
    if i%2 == 0:
        sum = sum + i
    i = i+1
print(sum)
# for Loop
sum = 0
for i in range(1,10):
    if(i%2 ==0 ):
        sum = sum+i
    i = i+1    
print(sum)