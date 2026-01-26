"""Write a program which accept one number and display below pattern.
    Input : 5
    Output :

"""


def Pattern(no):  
    for i in range(1, no + 2):
        for j in range(1, no +2 ):
            if(i > j):  
                print(j, end =" ")
        print()
def main():
    no = int(input("Enter number : "))

    Pattern(no)

    
if __name__ == "__main__":      
        main()

