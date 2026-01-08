def GuiseNumber(n):
    if(n==50):
        return "Correct You got the number !!!"
    elif(n>50):
        return "Guise number is too high!!"
    else:
        return "Guise number is too low!!!"

num=int(input("Enter number :"))
ans=GuiseNumber(num)
print(ans)