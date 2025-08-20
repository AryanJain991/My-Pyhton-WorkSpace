# # Question 12: Write a program to swap two numbers without using a temporary variable.

num1 = input("Please Enter First Num: ")
try:
    value1 = int(num1)

except ValueError:
    value1 = float(num1) 

num2 = input("Please Enter Second Num: ")
try:
    value2 = int(num2)

except ValueError:
    value2 = float(num2) 

print(f"\nBefore Swapping num1 = {value1}")
print(f"Before Swapping num2 = {value2}")

if num1 != num2:
    value1 = value1 + value2
    value2 = value1 - value2
    value1 = value1 - value2
    print(f"\nAfter Swapping num1 = {value1}")
    print(f"After Swapping num2 = {value2}")

else:
    print("Values are Equal After swapping the same value value will be same ")


# '''                         FOR THREE VARIABLES                            '''

# num1 = input("Please Enter First Num: ")
# try:
#     value1 = int(num1)

# except ValueError:
#     value1 = float(num1) 

# num2 = input("Please Enter Second Num: ")
# try:
#     value2 = int(num2)

# except ValueError:
#     value2 = float(num2) 

# num3 = input("Please Enter third Num: ")
# try:
#     value3 = int(num3)

# except ValueError:
#     value3 = float(num3) 

# print(f"\nBefore Swapping num1 = {value1}")
# print(f"Before Swapping num2 = {value2}")
# print(f"Before Swapping num2 = {value3}")

# if num1 != num2 and num2 != num3 and num3 != num1:
#     value1 = value1 - value3
#     value2 = value1 - value3
#     value3 = value1 + value2
#     print(f"\nAfter Swapping num1 = {value1}")
#     print(f"After Swapping num2 = {value2}")
#     print(f"After Swapping num3 = {value3}")

# else:
#     print("Values are Same For Each Variable After swapping the value will be same For Each Variable")