""" Write a program which accept one number and display below pattern. """

def Pattern(no):  
    for i in range(0, no + 1):
        for j in range(0, no +1 ):
            if(i < j):  
                print("*", end =" ")
        print()
def main():
    no = int(input("Enter number : "))

    Pattern(no)

    
if __name__ == "__main__":      
        main()


