# Given a tuple of integers, create:
# • A tuple of all even numbers
# • A tuple of all odd numbers
tup1=(2,3,4,5,6,7,8,9)
list1=[]
list2=[]
for i in tup1:
    if (i%2==0):
        list1.append(i)
    else:
        list2.append(i)
print(tuple(list1))
print(tuple(list2))