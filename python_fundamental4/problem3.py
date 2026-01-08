class Student:
    def __init__(self,name,roll_no,marks):
        self.__name=name
        self.__roll_no=roll_no
        self.__marks=marks
    def get_attr(self):
        return self.__name , self.__roll_no ,self.__marks
    def set_attr(self,mark,roll,name):
        self.__marks=mark
        if (self.__marks<0):
            print("Marks cannot be empty")
        else:
            print(f"updated marks is {self.__marks}")
        self.__roll_no=roll
        if (self.__roll_no<0 or self.__roll_no>100):
            print(" enter Roll no between 1 to 100")
        else:
            print(f"Roll no is {self.__roll_no}")
        self.__name=name
        if(self.__name==""):
            print("Name cannot be empty")
        else:
            print(f"Name is {self.__name}")

        
    

s1=Student("Ankit",101,93)
s1.set_attr(90,80,"Ankit")