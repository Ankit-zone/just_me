#  Given a list of words:
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# Create a dictionary that maps each word to its length.
# Example:
# {"apple": 5, "banana": 6, "kiwi": 4, ...}

words=["apple","banana","kiwi","cherry","mango"]

count=0
dict={}
for i in words:
    for j in i:
        count+=1
    dict.update({
        i:count
    })
    count=0

print(dict)