class Employee:         
        def __init__(self,name,salary):   #Constructor
                self.name= name 
                self.salary = salary

        @property  #This is how we create a getter method

        def first_name(self):     #This is a getter method
                l = self.name.split(" ")     #This will split the name into a list
                print(l)        #This will print the list
                return l[0]     #This will return the first element of the list with index 0
        
        @first_name.setter      #This is how we create a setter method

        def first_name(self,first):  #This is a setter method
                l = self.name.split(" ")  
                new_name = f"{first} {l[1]}"  #This will create a new name with the first name passed to the setter method and the last name from the original name
                self.name = new_name  #This will update the name attribute of the object


e = Employee("John Doe", 34555)
# print(e.first_name())

# e.set_first_name("Harry")
# e.first_name()
# print(e.name)

print(e.first_name) #This will call the getter method
e.first_name = "Harry"  #This will call the setter method
print(e.name)   
