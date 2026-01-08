# Write a function that takes two integers  and  and prints all even 
# numbers between them (inclusive).

def All_even(a,b):
    for i in range(a,b+1):
        if(i%2==0):
            print(i)


n1=int(input("Enter value of a :"))
n2=int(input("Enter value of b :"))

even=All_even(n1,n2)
print(even)