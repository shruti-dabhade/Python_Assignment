""". Write a program which accept one number and display below pattern. 
    Input : 5
    Output : 


"""


def main():
    no = int(input("Enter number "))
    
    for i in range(1, no+1):
        for j in range(1, no+1):
            print("*" ,end= " ")
        print()
if __name__ == "__main__":      
        main()