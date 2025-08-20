# Question 6: Write a Python program to compare two numbers and print the larger number. If both are equal, print that they are equal.

num1 = int(input("Pls Enter The First Num: ")) 
num2 = int(input("Pls Enter The Second Num: "))

if num1 < num2:
    print(f"The Larger Num is: {num2}")

elif num1 > num2:
    print(f"The Larger Num is: {num1}")

elif num1 == num2:
    print("They Are Equal")

else:
    ("The number is invalid") .capitalize()