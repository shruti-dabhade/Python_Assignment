"""
.Write a program which accept one number form user and return addition of its factors. 

    Input : 12 
    Output : 16
"""


def Factor(no):
      sum = 0
      for i in range(1, no):
            if(no % i == 0):
                  sum = sum + i
      return sum
def main():
    no = int(input("Enter number "))
    
    bRet = Factor(no)

    print("Sum of factor is : " ,bRet )
if __name__ == "__main__":      
        main()