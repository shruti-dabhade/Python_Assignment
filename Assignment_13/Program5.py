"""
Write a program which accepts marks and displays grade.
Condition Example:
• ≥ 75 → Distinction
• ≥ 60 → First Class
• ≥ 50 → Second Clas
• < 50 → Fail

"""

marks = int(input("Enter marks :"))

if(marks >= 75):
    print("Distinction")

elif(marks >= 60):
    print("First Class")

elif(marks >= 50):
    print("Second Clas")
else:
    print("fail")
