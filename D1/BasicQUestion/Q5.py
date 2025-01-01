# # Count how many vowels are in a given string using a loop.
word = input("enter a letter to check how many vowels are in  present: ").lower()
i = 0
vowelCount = 0
vowelletter = "aeiou"
while i <len(word):
    if(word[i] in vowelletter):
        vowelCount +=1
    i = i +1
print("Using while loop ____________ =", )    
print( "Total Number of Vowel letter in " , word  ," is :" , vowelCount)       

# in operator in Python is used to check membership in sequences such as strings, lists, tuples, sets, and dictionaries. 
# It evaluates to True if the specified element exists in the sequence and False otherwise.
# Check for a character in a string
# print('a' in 'apple')  # True
# # Check for a substring
# print('app' in 'apple')  # True

####################### for loop ###############

for i in range(len(word)):
    if word[i] in vowelletter :
        vowelCount +=1
print("Using for loop ___________________=")
print( "Total Number of Vowel letter in " , word  ," is :" ,  vowelCount)



     