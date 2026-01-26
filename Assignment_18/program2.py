"""Write a program which accept N numbers from user and store it into List. Return Maximum 
number from that List. 

"""

def Maximum(numbers):
    max = 0
    for num in numbers:
        if(num > max):
             max = num
    return max

def main():  
    n = int(input("Enter how many numbers you want: "))

    numbers = []
    for i in range(n):
        value = int(input(f"Enter number {i+1}: "))
        numbers.append(value)

    total = Maximum(numbers)
    print("Maximum element:", total)

    
if __name__ == "__main__":      
        main()
