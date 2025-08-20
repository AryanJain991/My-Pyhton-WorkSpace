# Question 4: Write a Python program to print the multiplication table of a number entered by the user.

num = 0
Table = int(input("Pls Enter the Number: "))
print("The table is: ")
while num < 10:
    num += 1
    var = Table * num
    print(f"{var}")