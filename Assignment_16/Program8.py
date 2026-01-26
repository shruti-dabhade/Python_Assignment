"""Write a program which accept number from user and print that number of “*” on screen.
    Input : 5
    Output : * * * * *
"""

def Pattern(no):  
    for i in range(1, no + 1):
         print("*", end =" ")
def main():
    no = int(input("Enter number : "))

    Pattern(no)

    
if __name__ == "__main__":      
        main()