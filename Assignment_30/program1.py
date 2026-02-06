"""Q1) Count Lines in a File
Problem Statement: 
Write a program which accepts a file name from the user and counts how many lines are present in the file.
Input: 
Demo.txt
Expected Output: 
Total number of lines in Demo.txt."""


import os

def CountLines(file_name):
    try:
        fobj = open(file_name, "r")
        count = 0

        for line in fobj:
            count += 1

        fobj.close()
        return count

    except FileNotFoundError:
        print("File not found")
        return 0


def main():
    file_name = input("Enter file name: ")

    if not os.path.exists(file_name):
        print("File does not exist")
        return

    result = CountLines(file_name)
    print(f"Total number of lines in {file_name}: {result}")


if __name__ == "__main__":
    main()
