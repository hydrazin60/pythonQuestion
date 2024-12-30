##Write a program to reverse a given string using a loop.
strings = "jiban"
i = len(strings) - 1
reverString = " "
while  i >=0:
    reverString = reverString + strings[i]   
    i -=1
print("While loop is ____________=")
print("reverse String is" , reverString)    


#  for loop

print("foor loop__________ =")
for i in range(len(strings)-1):
    reverString =  strings[i]  + reverString
print("reverse string is " , reverString)    
