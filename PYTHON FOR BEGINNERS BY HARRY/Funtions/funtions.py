# Program 1 function syntax

'''def fun_name():

    print("func() called")

print("Before Calling Function")
fun_name()
print("After calling Function ")'''

# program 2 In fUNCTION THERE IS NO NEED TO DEFINE THEIR TYPE LIKE C C++ AND JAVA IN PYTHON JUST SPECIFY THERE PARAMETERS.
'''
def date_of_independent_day(dd, mm, yyyy):
    print(dd, mm, yyyy, sep= "-")

print("India Became Independant On: ")
date_of_independent_day(15, "Aug" ,1947) '''

# Same Program Using Return

'''def get_date(d, m, y):
    return d + "-" + m + "-" + y

print("India Became Independant On: ")
m = get_date("15", "08" ,"1947")
print(m)'''

# Program 4 For Practicig 

'''def greet_msg():
    print("HI")
    print("Welcome To The GFG")

def exit_msg():
    print("Please Visit again")
    print("Bye")

greet_msg()
print("Hope You Are Enjoying")
exit_msg()'''

# HOW FUCTIONS WORKS??????????

'''def fun2():
    print("Inside the Fun2")

def fun1():
    print("before Fun2")
    fun2()
    print("After fun2")

print("Before Fun1")
fun1()
print("after fun1")'''

# Program 5 ;;;;;;;;;;;;;

'''def calc():
    x = 5
    y = 10
    x = x + 5
    print(x,y)

calc()
calc()'''

# DEFAULt Arguement If user does pass any value so:::::::::::::::::::::::----------------------

'''def printdetails(id, name = "NA", price = "NA"):
    print(f"Id is {id}")
    print(f"Name is {name}")
    print(f"Price is {price}")

printdetails(101,"ABC",100)
print()

printdetails(102)

print()
printdetails(103,"XYZ")'''

# Difference Between The Positional Arguement and Keyword Arguement----------------------------------

'''def printdetails(id, name, price):
    print(f"Id is {id}")
    print(f"Name is {name}")
    print(f"Price is {price}")

printdetails(101,"ABC",100)   #this is the positional argueeemnt
print()

printdetails(102, name = "aryan", price = 11000)     #thise is the mix postional and keyword arguemnetn

print()
printdetails(id = 103, name = "XYZ", price = 1045)   #this is the keyword arguement'''

# program 8 using variable length arguement ---------------------------------------------

'''def sum(*element):
    res = 0
    for x in element:
        res = res + x
    return res

print(sum(10,20))
print(sum(10,20,30))
print(sum(10))
print(sum())'''

# Program 9

'''def sum(init_sum,*element):
    res = init_sum
    for x in element:
        res = res + x
    return res

print(sum(10,20))
print(sum(10,20,30))
print(sum(10))'''


# Program 10 Using Keyword Length arguement in this sing ** to make it dictionary

def printDetails(**details):
    for key,value in details.items():
        print(f"{key} is {value}", end= ' ')


printDetails(id = 100, name = "Aryan", price = 10000)

print()

printDetails(id = 101, name = "Chirag", price = 110000)