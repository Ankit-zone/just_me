def calculator(a,b,op):
    if (op=="+"):
        return a+b
    elif(op=="-"):
        return a-b
    elif(op=="*"):
        return a*b
    elif(op=="/"):
        return a/b
    elif(op=="%"):
        return a%b
    else:
        return "Invalid Operation!"
    
n1=int(input("Enter First number :"))
n2=int(input("Enter second number :"))
operation=input("Enter operation : ")
ans=calculator(n1,n2,operation)
print("Required Answer is :",ans)