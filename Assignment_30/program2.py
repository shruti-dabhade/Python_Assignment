"""
    Q2) Count Words in a File
Problem Statement: 
Write a program which accepts a file name from the user and counts the total number of words in that file.
Input: 
Demo.txt
Expected Output: 
Total number of words in Demo.txt.

"""



import os

def CountWords(file_name):
    try:
        fobj = open(file_name, "r")
        data = fobj.read()
        fobj.close()

        words = data.split()
        return len(words)

    except FileNotFoundError:
        print("File not found")
        return 0


def main():
    file_name = input("Enter file name: ")

    if not os.path.exists(file_name):
        print("File does not exist")
        return

    result = CountWords(file_name)
    print(f"Total number of words in {file_name}: {result}")


if __name__ == "__main__":
    main()
