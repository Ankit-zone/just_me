class shape:
    def area(self):
        print("Area of shape class!!")
class circle(shape):
    def area(self,radious):
        self.radious=radious
        area=3.14*self.radious**2
        print(f"Area of circle! is ={area}")
class Rectangle(circle):
    def area(self,length,breadth):
        self.length=length
        self.breadth=breadth
        area=self.length*self.breadth
        print(f"Area of rectangle is ={area}")
class Triangle(shape):
    def area(self,base,height):
        self.base=base
        self.height=height
        area=1/2*self.base*self.height
        print(f"Area of Triangle is ={area}")

ar1=Rectangle()
ar1.area(5,6)