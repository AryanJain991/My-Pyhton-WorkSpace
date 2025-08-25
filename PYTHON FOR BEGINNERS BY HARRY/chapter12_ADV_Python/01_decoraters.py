def decorator(func): # This is a decorator function
    def wrapper():  # This is a nested function
        print("I am about to execute the function") 
        func()  # This will execute the function passed to the decorator
        print("I have executed the function")
    return wrapper      

@decorator      # This is how we use a decorator
def say_hello():
    print("Hello")

say_hello()


# F = decorator(say_hello)  #This is how we use a decorator
# F()