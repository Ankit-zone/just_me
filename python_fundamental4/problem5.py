class Vehical:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Car(Vehical):
    def count_seat(self,seats):
        self.seats=seats
        print(f"Brand is {self.brand},Model is {self.model} and no of seats are {self.seats}")
class Bike(Vehical):
    def engine_cc(self,cc):
        self.cc=cc
        print(f"Bike brand is {self.brand},Model is {self.model} and engine cc is {self.cc}")

ob1=Bike("splendor",2012)
ob1.engine_cc(125)