class employee:
    company = "Hp"

    def get_salary(self):
        return 34000
    
e = employee()
print(e.get_salary())

e1 = employee()
print(e.get_salary())
print(e1.company)