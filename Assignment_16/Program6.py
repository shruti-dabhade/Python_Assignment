"""
Write a program which accept number from user and check whether that number is positive or 
negative or zero.

    Input : 11    
    Output : Positive Number
    Input : -8   
    Output : Negative Number  
    Input : 0       
    Output : Zero 
    
"""

def CheckNum(no):
      
    if(no == 0):
        print("Zero")
    elif(no < 0):
         print("Negative number")  
    else:
         print("Positive number")
    
       
def main():
    no = int(input("Enter number : "))
    CheckNum(no)

    
if __name__ == "__main__":      
        main()