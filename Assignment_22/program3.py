"""Write a Python program to implement a class named Arithmetic with the following 
characteristics:
    • The class should contain two instance variables: Value1 and Value2.
    • Define a constructor (__init__) that initializes all instance variables to 0.
    • Implement the following instance methods:
    ◦ Accept() – accepts values for Value1 and Value2 from the user.
    ◦ Addition() – returns the addition of Value1 and Value2.
    ◦ Subtraction() – returns the subtraction of Value1 and Value2.
    ◦ Multiplication() – returns the multiplication of Value1 and Value2.
    ◦ Division() – returns the division of Value1 and Value2 (handle division by zero 
    properly).
    • Create multiple objects of the Arithmetic class and invoke all the instance methods

    """

class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = float(input("Enter value 1: "))
        self.Value2 = float(input("Enter value 2: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 == 0:
            return "Division by zero not allowed"
        else:
            return self.Value1 / self.Value2


Obj1 = Arithmetic()
Obj2 = Arithmetic()


Obj1.Accept()
print("Addition:", Obj1.Addition())
print("Subtraction:", Obj1.Subtraction())
print("Multiplication:", Obj1.Multiplication())
print("Division:", Obj1.Division())

print("-----------------------")


Obj2.Accept()
print("Addition:", Obj2.Addition())
print("Subtraction:", Obj2.Subtraction())
print("Multiplication:", Obj2.Multiplication())
print("Division:", Obj2.Division())
