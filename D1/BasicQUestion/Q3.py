# # Print the multiplication table of a given number.
num = int(input("Which number do you want to multiply? "))
i = 1
table = 0
while i <=10:
    table = num * i
    print("The table of", num, "is:", num, "*", i, "=", table)
    i += 1

# for loop
for i in range(1,11):
    table = i * num
    print("The table of", num, "is:", num, "*", i, "=", table) 