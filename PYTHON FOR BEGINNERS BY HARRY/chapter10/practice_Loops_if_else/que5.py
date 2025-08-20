# Question 5: Write a Python program to check if a number is divisible by both 3 and 5.

num = int(input("Pls enter a num: "))

if num % 3 == 0:
    print("the num is divisible by 3")

elif num % 5 == 0:
    print("The num is divisible by 5")

else:
    print("The Num is not divisible by both 3 and 5 ")
