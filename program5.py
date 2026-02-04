""" Compare Two Files (Command Line)

    Problem Statement: 
    Write a program which accepts two file names through command line arguments and compares the contents of 
    both files.
    • If both files contain the same contents, display Success
    • Otherwise display Failure

    Input (Command Line): 
    Demo.txt Hello.txt
    Expected Output: 
    Success OR Failur
"""
import sys
import os

def CompareFile(source1, source2):
    f1 = open(source1, "r")
    data1 = f1.read()
    f1.close()

    f2 = open(source2, "r")
    data2 = f2.read()
    f2.close()

    if data1 == data2:
        print("Success")
    else:
        print("Failure")


def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py <File1> <File2>")
        return

    source_file1 = sys.argv[1]
    source_file2 = sys.argv[2]

    if not os.path.exists(source_file1):
        print("Source file 1 does not exist")
        return

    if not os.path.exists(source_file2):
        print("Source file 2 does not exist")
        return

    CompareFile(source_file1, source_file2)


if __name__ == "__main__":
    main()
