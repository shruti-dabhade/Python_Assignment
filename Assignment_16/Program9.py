""". Write a program which display first 10 even numbers on screen. 
 Output : 2 4 6 8 10 12 14 16 18 20 
"""



def DisplayEven(no):  
    for i in range(1, no + 1):
         if(i % 2 == 0):
              print(i , end=" ")


def main():
    no = int(input("Enter number : "))

    DisplayEven(no)

    
if __name__ == "__main__":      
        main()