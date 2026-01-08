def Print_Digit(n):
    d=0
    while(n>0):
        d=n%10
        n//=10
        print(d)

num=int(input("Enter number :"))

print(Print_Digit(num))