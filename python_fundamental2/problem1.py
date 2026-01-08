# Write a program that takes  as input. Using conditional statements, 
# calculate the  
# final tax rate
# based on these rules:
# • 
# If salary < 30,000 → 5%
# • 
# If salary is 30,000–70,000 → 15%
# • 
# If salary > 70,000 → 25%

salary=float(input("Enter salary :"))

if salary<30000:
    rate1=salary*5/100
    print("Tax rate on Salary :",rate1)
elif salary>=30000 and salary <=70000:
    rate2=salary*15/100
    print("Tax rate on salary :",rate2)
else:
    rate3=salary*25/100
    print("Tax rate on salary :",rate3)

