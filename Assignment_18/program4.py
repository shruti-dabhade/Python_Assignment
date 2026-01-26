""".Write a program which accept N numbers from user and store it into List. Accept one another 
number from user and return frequency of that number from List. 
    Input : Number of elements : 11 
    Input Elements : 13 5 5 4 22 33 5  
    Element to search : 5 
    Output : 3
"""


def  Search(numbers, no):
    count = 0
    for num in numbers:
        if(num == no):
             count = count + 1
    return count

def main():  
    n = int(input("Enter how many numbers you want: "))

    numbers = []
    for i in range(n):
        value = int(input(f"Enter number {i+1}: "))
        numbers.append(value)

    search_no = int(input("Enter element to search "))
    iRet = Search(numbers, search_no)
    print("Number of time element occur ", iRet)

    
if __name__ == "__main__":      
        main()
