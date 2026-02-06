"""Q5) Search a Word in File
Problem Statement: 
Write a program which accepts a file name and a word from the user and checks whether that word is present in 
the file or not.
Input: 
Demo.txt Marvellous
Expected Output: 
Display whether the word Marvellous is found in Demo.txt or not."""

import os

def SearchWord(file_name, word):
    try:
        fobj = open(file_name, "r")
        data = fobj.read()
        fobj.close()

        if word in data:
            return True
        else:
            return False

    except FileNotFoundError:
        print("File not found")
        return False


def main():
    file_name = input("Enter file name: ")
    word = input("Enter word to search: ")

    if not os.path.exists(file_name):
        print("File does not exist")
        return

    result = SearchWord(file_name, word)

    if result:
        print(f'Word "{word}" is found in {file_name}')
    else:
        print(f'Word "{word}" is not found in {file_name}')


if __name__ == "__main__":
    main()
