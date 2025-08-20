# Question 10: Write a program to calculate the factorial of a number entered by the user.

fact = int(input("Pls Enter The No.: "))

while True:
    value = fact + (fact - 1) + (fact - 2) 
    value -= 1
    print(value)