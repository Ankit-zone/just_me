#  Design a program to continuously input a number  from user & print if it is 
# positive or negative until the user enters “Quit”.
n=int(input("Enter number pos or neg :"))
while(n):
    if(n=="Quit"):
        break
    else:
        print(n)
    n=input("Enter Again:")
