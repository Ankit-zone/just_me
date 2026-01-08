# Create a dictionary where:
# • Keys = student names
# • Values = marks (integer)
# Write a menu-based program where user presses a key (’A’, ‘B’, ‘C’, ‘D’)
# depending on the operation they want to perform on the dictionary:
# 1. A - Add a student
# 2. B - Update marks
# 3. C - Search for a student
# 4. D - Display all students and marks

dict={"Ankit" : "95","Amit":"92","Ashish":"99","Ritik":"96"}
key=input("A - Add a student\nB - Update marks\nC - Search for a student\nD - Display all students and marks\nEnter :")

if(key=='A'):
    student=input("Enter Student name :")
    dict.update({
        student:None
    })
elif(key=='B'):
    val=input("Enter Student name whose marks you want to change :")
    marks=input("Enter Marks :")
    dict[val]=marks
    print(dict)
elif(key=='C'):
    student1=input("Enter the student name you want to search :")
    print(dict.get(student1))
else:
    print(dict)