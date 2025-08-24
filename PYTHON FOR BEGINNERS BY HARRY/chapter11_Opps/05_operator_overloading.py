class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self,p):
        return Point((self.x + p.x) , (self.y + p.y)) 
    
    # def __add__(self, p):
    #     return Point((self.x + p.x) , (self.y + p.y))
    
    def print_point(self):
        return(f"The point is ({self.x} , {self.y})")
    
    def __add__(self, p):      #This is how we overload the + operator
        return Point((self.x + p.x) , (self.y + p.y))

p1 = Point(3,2)
p2 = Point(6,3)

p = p1+p2 #we overloaded the + operator
                    
print(p.print_point())







class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self,p):
        return Point((self.x + p.x) , (self.y + p.y)) 
    
    # def __add__(self, p):
    #     return Point((self.x + p.x) , (self.y + p.y))
    
    def print_point(self):
        return(f"The point is ({self.x} , {self.y})")

p1 = Point(3,2)
p2 = Point(6,3)

p = p1.sum(p2) #return new points which is the sum of p1 and p2
print(p.print_point())