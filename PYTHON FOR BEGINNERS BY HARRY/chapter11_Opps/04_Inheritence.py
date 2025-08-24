class Animal:
    location = "India"

    def __init__(self,name):
        self.name = name
    
    def speak(seld):
        print("Speaking Now....")

class Dog(Animal):        #This Is how ingeritence is done in python
    def speak(self):
        super().speak()     #This will call the speak method of the parent class
        print("Bark Bark!!")


# a = Animal("Dog")
# a.speak()
# print(a.location)

a = Dog("Bruno")
a.speak()
print(a.location)