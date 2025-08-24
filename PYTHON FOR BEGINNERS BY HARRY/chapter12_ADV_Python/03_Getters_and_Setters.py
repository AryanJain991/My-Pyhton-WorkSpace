class Employee:
        def __init__(self,name,salary):
                self.name= name 
                self.salary = salary

        @property  #This is how we create a getter method

        def first_name(self):
                l = self.name.split(" ")
                print(l)
                return l[0]
        
        @first_name.setter      #This is how we create a setter method

        def first_name(self,first):
                l = self.name.split(" ")
                new_name = f"{first} {l[1]}" 
                self.name = new_name


e = Employee("John Doe", 34555)
# print(e.first_name())

# e.set_first_name("Harry")
# e.first_name()
# print(e.name)

print(e.first_name) #This will call the getter method
e.first_name = "Harry"  #This will call the setter method
print(e.name)   
