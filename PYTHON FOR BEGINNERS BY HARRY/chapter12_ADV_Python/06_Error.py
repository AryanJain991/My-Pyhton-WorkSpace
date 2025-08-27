'''This Is Our first Method Using Exception Errors'''

# while True:     # infinite loop
#     try:
#         a = int(input("Enetr a Number 1: "))
#         b = int(input("Enetr a Number 2: "))

#         print(f"the division of these two num {a/b}")

#     except ValueError:
#         print("Pls Enter only Integer value!!! don't try to convert a name into integer")

#     except ZeroDivisionError:
#         print("Don't Devide a num using 0")

#     except Exception as e:
#         print("Sry There is Some Error Pls Try Again!!!!!!")



'''This Is Our Second Method Using Raise Exception'''

# a = int(input("Enetr a Number 1: "))
# b = int(input("Enetr a Number 2: "))

# if b == 0:
#     raise ValueError("don't divide with 0")

# print(f"the division of these two num {a/b}")



'''This Is Our Third Method Using Else and Finally  '''
'''USing With Else'''
# try:
#     a = 345/10

# except Exception as e:
#     print(e)

# else:
#     print("It is successfully divided")



'''USing With Finally'''

while True:
    def divide(a,b):
        try:    
            c = a/b
            print(c)
            return(c)
        
        except Exception as e:
            print(e)
            return None

        finally:
            print("Finally - Prints always whatever inside the finally no matter error occur or not")

    a = int(input("Pls Enter a num 1: ")) 
    b = int(input("Pls Enter a num 2: ")) 

    divide(a,b)
    
    

