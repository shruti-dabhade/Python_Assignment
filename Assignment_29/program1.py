""" Check File Exists in Current Directory
    Problem Statement: 
    Write a program which accepts a file name from the user and checks whether that file exists in the current 
    directory or not.
        Input: 
        Demo.txt
        Expected Output: 
        Display whether Demo.txt exists or not
        
    """


import os

def main():
    file_name = input("Enter file name: ")
    open(file_name,"w")

    if os.path.exists(file_name):
        print(f"{file_name} exists")
    else:
        print(f"{file_name} does not exist")

if __name__ == "__main__":
    main()
