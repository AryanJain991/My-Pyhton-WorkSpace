def decorator(func):
    def wrapper():
        print("I am about to execute the function")
        func()
        print("I have executed the function")
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()


# F = decorator(say_hello)  #This is how we use a decorator
# F()