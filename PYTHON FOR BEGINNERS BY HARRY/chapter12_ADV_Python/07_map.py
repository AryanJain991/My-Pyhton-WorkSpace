numbers = [1,3,5,45,95,0]

def square(x):
    return x * x

new = list(map(square,numbers))
print(new)