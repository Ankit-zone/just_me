#Write a program to Calculate Area of Scalene Triangle.
a= int(input("enter first side of scalene triangle = "))
b= int(input("enter second side of scalene triangle = "))
c= int(input("enter third side of scalene triangle = "))

s = (a+b+c)/2

print("semiperimeter = ",s)

A = ((s*(s-a)*(s-b)*(s-c))**(1/2))

print("Area of scalene triagle = ",A)
