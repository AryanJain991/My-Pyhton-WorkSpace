# Question 1: Write a function factorial(n) that calculates and returns the factorial of a given number.

# n = int(input("Pls Enter a Number: "))

# result = 1

# for i in range(1, n + 1):
#     result = result * i

# print("Factorial is:", result)



n = int(input("Pls Enter a Number: "))

result = 1
count = 1

while count < n:
    result = result * count 
    count += 1
print(result)