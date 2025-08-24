class Employee:

    def __init__(self,name,salary,bond):
        self.name = name
        self.salary = salary
        self.bond = bond
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name} and his salary is {self.salary} and bond is {self.bond} years")



e = Employee("John Doe", 34000, 4)
e.get_info()