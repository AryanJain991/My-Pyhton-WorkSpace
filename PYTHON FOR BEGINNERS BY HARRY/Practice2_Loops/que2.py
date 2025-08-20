# 2. Sum of Even Numbers using for loop
# Write a Python program that uses a for loop to calculate the sum of all even numbers from 1 to 50.

sum_even = 0
for i in range(2,51,2):
    print(i,end=' ')
    sum_even += i
print(f"\nSum of Even Num bet 1 to 50: {sum_even}")

'''           using remainder and if         '''

# sum_even = 0
# for i in range(1,51):
#     if i % 2 == 0:
#         sum_even += i
# print(f"Sum of Even Num bet 1 to 50: {sum_even}")

'''            Using Print and Sum             '''

# sum_even = 0
# for i in range(1,51):
#     if i % 2 == 0:
#         print(i, end=' ')
#         sum_even += i
# print("\nsum:",sum_even)

