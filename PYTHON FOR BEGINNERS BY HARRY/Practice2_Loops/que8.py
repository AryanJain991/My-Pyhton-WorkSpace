# 9. Sum of Digits using while loop
# Write a Python program that takes a number as input and calculates the sum of its digits using a while loop.

num = int(input("Pls Enter A Number: "))

digit_sum = 0

while num > 0:
    digit = num % 10
    digit_sum = digit_sum + digit
    num = num // 10
    var = num + digit_sum
print(var)
# print(digit_sum)
    

