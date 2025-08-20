# 7. Count Digits in a Number using while loop
# Write a Python program that takes a number as input and uses a while loop to count how many digits it has.

# num = int(input("Pls Enter A Number: "))
# count = 0
# digit_sum = 0

# while num > 0:
#     digit = num % 10
#     digit_sum += digit

#     count += 1
#     num = num // 10

# print("",digit_sum)
# print("Total Digits:", count)




num = int(input("Pls Enter A Number: "))
count = 0
digit_sum = 0

while num > 0:
    digit = num % 10        
    digit_sum += digit

    count += 1
    num = num // 10

print("Total Digits:", count)
print("Sum of Digits:", digit_sum)
