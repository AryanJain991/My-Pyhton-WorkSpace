# numbers = [1,3,5,45,95,0]

# def square(x):
#     return x * x

# new = list(map(square,numbers))
# print(new)


"""Lambda uses with map == it helps to reduce the no of lined in our program"""


numbers = [1,3,5,45,95,0]

new = list(map(lambda x: x*x,numbers))
print(new)
