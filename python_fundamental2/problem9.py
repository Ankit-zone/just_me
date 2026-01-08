def is_prime(n):
    if(n<2):
        return "Invalid"
    for i in range(2,n-1):
        if(n%i==0):
            return "Not Prime"
    return "prime"

num=int(input("Enter number :"))

ans=is_prime(num)
print("Number is :",ans)