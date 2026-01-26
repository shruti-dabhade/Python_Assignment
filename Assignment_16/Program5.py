"""  
Write a program which display 10 to 1 on screen
Output : 10, 9 , 8, 7, 6, 5, 4, 3, 2, 1 

"""

def Display(no):
    for i in range(no, 0, -1):
        print(i ,end =" ")
       
def main():
    no = int(input("Enter number : "))
    Display(no)

    
if __name__ == "__main__":      
        main()