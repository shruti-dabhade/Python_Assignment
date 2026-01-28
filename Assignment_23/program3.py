""" Write a Python program to implement a class named Numbers with the following 
specifications:
• The class should contain one instance variable:
◦ Value
• Define a constructor (__init__) that accepts a number from the user and initializes Value.
• Implement the following instance methods:
◦ ChkPrime() – returns True if the number is prime, otherwise returns False
◦ ChkPerfect() – returns True if the number is perfect, otherwise returns False
◦ Factors() – displays all factors of the number
• Create multiple objects and call all methods.
◦ SumFactors() – returns the sum of all factors 
(You may use this method as a helper in ChkPerfect() if required"""


class Numbers:

    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total

    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        else:
            return False

Obj1 = Numbers()
Obj2 = Numbers()

print("Is Prime:", Obj1.ChkPrime())
Obj1.Factors()
print("Is Perfect:", Obj1.ChkPerfect())



print("Is Prime:", Obj2.ChkPrime())
Obj2.Factors()
print("Is Perfect:", Obj2.ChkPerfect())
