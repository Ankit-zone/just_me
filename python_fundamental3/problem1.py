#  Ask the user for a string and check whether it is a palindrome or not.
# A is a string which is same when we read it forward & backward. Eg -
# “madam”, “racecar” etc.

str1=input("Enter String :")

str2=str1[::-1]

if (str1==str2):
    print("Yes! It is palindrome!")
else:
    print("No It is not a palindrome!")
