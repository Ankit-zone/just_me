class Person:
    def __init__(self,name,age=None,address=None): # Default parameter 
        self.name=name
        self.age=age
        self.address=address
    def display(self):
        print(f"Name is {self.name}")
        if (self.age!=None):
            print(f"Age is {self.age}")
        if (self.address!=None):
            print(f"Address is {self.address}")
p1=Person("Ankit")
p2=Person("Ankit",20)
p3=Person("Ankit",20,"Gorakhpur")

p1.display()
