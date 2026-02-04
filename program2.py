""" Display File Contents
    Problem Statement: 
    Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the 
    console.
        Input: 
        Demo.txt
        Expected Output: 
        Display contents of Demo.txt on console

"""


import os

def main():
    file_name = input("Enter file name: ")
    try:
        if os.path.exists(file_name):
            print(f"{file_name} exists")
        else:
            print(f"{file_name} does not exist")

        fobj = open(file_name)
        print("File opened!!")

        Data = fobj.read()

        print("Data from file : ", Data)
    except FileNotFoundError:
        print("Error occure while reading data from file")



if __name__ == "__main__":
    main()
