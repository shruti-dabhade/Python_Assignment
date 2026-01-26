"""Write a program which accept N numbers from user and store it into List. Return addition of all 
elements from that List. """

def Addition(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
def main():
    
      
    n = int(input("Enter how many numbers you want: "))

    numbers = []
    for i in range(n):
        value = int(input(f"Enter number {i+1}: "))
        numbers.append(value)

    total = Addition(numbers)
    print("Addition of all elements:", total)

    
if __name__ == "__main__":      
        main()
