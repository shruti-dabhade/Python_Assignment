"""Write a program which accept N numbers from user and store it into List. Return Minimum 
number from that List. 

"""

def  Minimum(numbers):
    min = 9
    for num in numbers:
        if(num < min):
             min = num
    return min

def main():  
    n = int(input("Enter how many numbers you want: "))

    numbers = []
    for i in range(n):
        value = int(input(f"Enter number {i+1}: "))
        numbers.append(value)

    min = Minimum(numbers)
    print("Minimum element:", min)

    
if __name__ == "__main__":      
        main()
