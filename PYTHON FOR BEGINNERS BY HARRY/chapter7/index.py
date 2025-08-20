# for i in range(1,10):
#     print(i)

# list = ["Rohan", "Shubhi", "manoj", "Jain", "Niru", "Jambu"]
# i = 0

# while(i < len(list)):
#     print(list[i])
#     i +=1

# for i in range(100):
#     if i == 34:
#         break
#     print(i)

# for i in range(100):
#     if i == 34:
#         continue
#     print(i)

# n = int(input("Enter a num "))
# i = 1
# while i<11:
#     print(f"{n} X {i} = {n * i}")
#     i += 1

# n = int(input("Enter a num "))
# for i in range(11):
#     print(f"{n} X {i} = {n * i}")
    

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if name.startswith("S"):
#         print(f"Hello {name}")


# n = int(input("Enter a Number: "))

# for i in range(2, n):
#     if (n % i) == 0:
#         print("Number Is Not Prime")
#         break

# else:
#     print("Number Is Prime")


# n = int(input("Enter a num: "))

# for i in range(2, n):
#     if(n % i) == 0:
#         print("num is not prime ")
#         break

# else:
#     print("num is prime")

# n = int(input("Enter a Num: "))

# i = 1
# sum = 0

# while(i<=n):
#     sum+=i
#     i+=1

# print(sum)

# n = int(input("Enter The Num:   "))

# product = 1

# for i in range(1, n+1):
#     product = product * i
# print(f"The factorial of {n} is {product}")

# n = int(input("Enter The Num:   "))

# for i in range(1, n+1):
#     print(" " * (n-i), end="")
#     print("*" * (2*i-1), end="")
#     print("")  


# n = int(input("Enter The Num:   "))

# for i in range(1, n+1):
#     print("*" * i, end="")
#     print("")  

# n = int(input("Enter The Num:   "))

# for i in range(1, n+1):
#     if(i == 1 or i == n):
#         print("*" * n, end="")
#     else:
#         print("*",end="")
#         print(" "* (n-2),end="")
#         print("*",end="")
#     print("")


n = int(input("Enter The Num:   "))
for i in range(1,11):
    print(f"{n} * {11-i} = {n*(11-i)}")