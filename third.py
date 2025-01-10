#Write a program to find gross salary.
a = int(input("enter the basic sallary :"))

HRA = (20*a)/100
DA = (50*a)/100
TA = (5*a)/100

sallary = a + HRA + DA + TA
print("Gross sallary =",sallary)
