class Employee:
    comapny = "Aryan PVT LTD"
    def __init__(self, name, salary):  # Constructor
        self.name = name  # Instance variable
        self.salary = salary  # Instance variable

    # instance method
    def print_info(self):
        print(f"Name is {self.name} and salary is {self.salary} and company is {self.comapny}")

    # static method
    @staticmethod # Static method
    def sum(a,b):   # Static method does not take self or cls as first argument
        return f"Value of a is {a} and value of b is {b} and their sum is = {a+b}"
    
    # class method
    @classmethod
    def print_company(cls): # Class method takes cls as first argument
        return f"The company name is {cls.comapny}"
    
    @classmethod
    def change_company(cls,new_company): # Class method takes cls as first argument
        cls.comapny = new_company

        


e1 = Employee("Aryan", 34555)
e2 = Employee("Harry", 45566)

e1.print_info()
e2.print_info()

print(e2.sum(4,5)) # Static method can be called using object
print(Employee.sum(4,5)) # Static method can be called using class name

e1.print_company()


e1.change_company("Harry PVT LTD")
print(e1.print_company())