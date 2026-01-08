# Write a program that takes a string from the user and prints the number of
# spaces in the string.

str1=input("Enter string :")
a=len(str1)
b=str1.replace(" ","")
b=len(b)
c=a-b
print(f"No of spaces in string is :{c}")