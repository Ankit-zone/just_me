#Given a list of integers compute the average of all numbers in the list.

lists=[5,8,7,9,4,6,7,8]
sum=0
count=0
for i in lists:
    count+=1
    sum+=i

avg=sum/count
print(f"Avg of list is {avg}")