# 3. Print Multiplication Table using for loop
# Write a Python program that takes a number as input and uses a for loop to print its multiplication table (from 1 to 10).

num_table = int(input("Pls Enter a Number: "))

for i in range(1,11,1):
    table = num_table * i
    print(table)