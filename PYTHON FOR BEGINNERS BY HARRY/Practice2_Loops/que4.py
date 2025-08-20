# 4. Print Prime Numbers from 1 to 100 using for loop
# Write a Python program that prints all prime numbers between 1 and 100 using a for loop.

for i in range(1,101):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)

