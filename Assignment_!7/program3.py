"""Write a program which accept one number from user and return its factorial. 
        Input : 5
        Output : 120
    
"""



def main():
    no = int(input("Enter number "))
    
    fact = 1

    for i in range(1, no +1):
          fact = fact * i
    
    print("Fcatorial is : " , fact)
if __name__ == "__main__":      
        main()