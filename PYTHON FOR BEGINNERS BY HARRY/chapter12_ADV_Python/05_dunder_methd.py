class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def __str__(self):      # This is used to print the object in a user friendly way
        return f"Name is {self.name} and salary is {self.salary}"
    
    def __repr__(self):    # This is used for debugging and logging
        return f"name: {self.name}\nsalary: {self.salary}"
    
    def __len__(self):      # This will return the length of the name
        return len(self.name)


e = Employee("Aryan", 34555) 
print(e.name, e.salary) 
print(str(e))
print(repr(e))
print(len(e))