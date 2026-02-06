""" 
 Frequency of a String in File
Problem Statement: 
Write a program which accepts a file name and one string from the user and returns the frequency (count of 
occurrences) of that string in the file.
Input: 
Demo.txt Marvellous
Expected Output: 
Count how many times "Marvellous" appears in Demo.txt
"""
import sys
import os

def CountFrequency(file_name, search_string):
    fobj = open(file_name, "r")
    data = fobj.read()
    fobj.close()

    count = data.count(search_string)
    return count


def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py <FileName> <String>")
        return

    file_name = sys.argv[1]
    search_string = sys.argv[2]

    if not os.path.exists(file_name):
        print("File does not exist")
        return

    result = CountFrequency(file_name, search_string)
    print(f'Frequency of "{search_string}" in {file_name} is: {result}')


if __name__ == "__main__":
    main()
