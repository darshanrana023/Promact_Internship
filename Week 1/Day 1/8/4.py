# Python program to find the largest number among the three input numbers

num1=int(input("Enter First Integer"))
num2=int(input("Enter Second Integer"))
num3=int(input("Enter Third Integer"))

if (num1>=num2) and (num1>=num3):
    largest= num1
elif(num2>=num1) and (num2>=num3):
    largest= num2
else:
    largest= num3 
 
print("Largest number among this three numbers is:",largest)
