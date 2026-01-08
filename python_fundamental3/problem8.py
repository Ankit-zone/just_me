#Write a program to check whether two lists share no common elements.
# share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
# share common elements list1 = [1, 2, 3] list2 = [3, 4]

list1=[1,2,3,4]
list2=[5,6,7]

list3=list1+list2
set1=set(list3)
list4=list(set1)
if(list4==list3):
    print("No common Element!!")
else:
    print("Share common element!!")