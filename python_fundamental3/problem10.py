# Ask the user for a string and print:
# • All unique characters
# • The count of unique character

str1=input("Enter a String :")
s=str()
count=0
for i in str1:
    if i not in s:
        s+=i
        count+=1

print(f"These are the all unique character in string : {s}")
print(f"No of unique character is : {count}")




