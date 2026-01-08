#Write a program to swap values of two numbers entered by the user.

num1=int(input("Enter first num : "))
num2=int(input("Enter second num : "))
print("Before Swap\n")
print("First num :",num1)
print("Second num :",num2)
temp=num1
num1=num2
num2=temp
print("\nAfter Swap\n")
print("First num :",num1)
print("Second num :",num2)