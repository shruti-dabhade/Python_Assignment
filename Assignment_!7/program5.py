"""5.Write a program which accept one number for user and check whether number is prime or not.
    Input : 5
    Output : It is Prime Number 
"""

def Prime(no):
    bFlag = True

    for i in range(2,no ):
         if(no % i == 0):
              bFlag = False
    if(bFlag == True):
         print("Number is prime")
    else:
         print("Number is not prime")
def main():
    no = int(input("Enter number "))
    
    Prime(no)
if __name__ == "__main__":      
        main()