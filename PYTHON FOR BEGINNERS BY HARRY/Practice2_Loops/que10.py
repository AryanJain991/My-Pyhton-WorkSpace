# result = 1
# for i in range(1,4):
#     result *= 1
# print(result)

# sum = 0
# for i in range(1,6):
#     sum+=i
# print(sum)


# 10. Print Fibonacci Series using while loop
# Write a Python program that uses a while loop to print the first 10 terms of the Fibonacci series.

# count = 0

# a = 0
# b = 1

# while  count < 10:
#     print(a)    

#     c = a + b
#     a = b
#     b = c
#     count = count + 1


a = 0
b = 1

for i in range(0,10):
    print(a, end=" ")
    c = a+b
    a = b
    b = c