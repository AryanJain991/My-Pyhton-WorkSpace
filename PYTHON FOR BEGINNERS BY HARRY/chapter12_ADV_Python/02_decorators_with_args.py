def repeat(n):  # This is a decorator factory that takes an argument n
    def decorator(func):  # This is the actual decorator
        def wrapper(a):   # This is the wrapper function that will replace the original function
            for i in range(n): # This will repeat the function n times
                func(a)  # This will call the original function
        return wrapper
    return decorator
     
@repeat(7)    # This is how we use a decorator with arguments
def say_hello(a): 
    print(f"Hello!!{a}")

say_hello("Harry")
