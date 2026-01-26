""". Write a program which accept number from user and return number of digits in that number. 
    Input : 1234
    Output : 4
"""


def CountDigit(no):  
    iDigit = 0
    count = 0
    while(no != 0):
         iDigit = no % 10
         count = count + 1
         no = no // 10
    return count
         
def main():
    no = int(input("Enter number : "))

    iRet = CountDigit(no)

    print("Number of digits are : ", iRet)
    
if __name__ == "__main__":      
        main()

