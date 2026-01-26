"""
Write a program which display 5 times Marvellous on screen. 
    Output : 
    Marvellous 
    Marvellous 
    Marvellous 
    Marvellous 
    Marvellous  
"""

def Display(no):
      for i in range(1, no + 1):
            print("Marvellous")
      

def main():
    no = int(input("Enter number : "))
    Display(no)


if __name__ == "__main__":      
        main()