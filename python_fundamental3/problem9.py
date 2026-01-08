# Given a list, print all elements that appear more than once in the list.

list1=[1,2,2,3,3,4,4]
d=set()
dup=[]
for i in list1:
    if i in d:
        dup.append(i)
    else:
        d.add(i)
print(dup)
print(d)