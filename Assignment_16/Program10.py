""" Write a program which accept name from user and display length of its name.
    Input : Marvellous   
    Output : 10 
"""


def Display(str):  
   return len(str)


def main():
    str = input("Enter name : ")

    length = Display(str)
    print("Length is : ", length)

    
if __name__ == "__main__":      
        main()