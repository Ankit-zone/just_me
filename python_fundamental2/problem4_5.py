n=int(input("Enter number :"))
sum=0
count=0
while(n>0):
    sum+=n%10
    count+=1
    n//=10
print(sum)
print(count)
