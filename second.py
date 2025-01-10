#Write a program to Calculate Sum of 5 Subjects and Find Percentage.
sub1 = int(input("enter the number of maths:"))
sub2 = int(input("enter the number of english :"))
sub3 = int(input("enter the number of chemistry:"))
sub4 = int(input("enter the number of physics:"))
sub5 = int(input("enter the number of hindi:"))

sum = sub1+sub2+sub3+sub4+sub5

prsnt = (sum/500)*100

print(" Total Percentage = ",prsnt)
