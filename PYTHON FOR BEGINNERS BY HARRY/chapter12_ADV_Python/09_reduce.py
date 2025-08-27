from functools import reduce

# numbers = [1, 2, 5, 6, 8, 9, 41, 54, 99, 54]

# def sum(a,b):
#     return a + b

# c = reduce(sum, numbers)
# print(c)

"""let's see with lambda function"""

numbers = [1, 2, 5, 6, 8, 9, 41, 54, 99, 54]
 
c = reduce(lambda a,b : a+b , numbers)
print(c)
