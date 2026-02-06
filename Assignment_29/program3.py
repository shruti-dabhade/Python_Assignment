"""  Copy File Contents into a New File (Command Line)
    Problem Statement: 
    Write a program which accepts an existing file name through command line arguments, creates a new file 
    named Demo.txt, and copies all contents from the given file into Demo.txt.
    Expected Output: 
    Create Demo.txt and copy contents of ABC.txt into Demo.txt

"""

import sys
import os

def CopyFile(source, destination):
    fsrc = open(source, "r")
    data = fsrc.read()
    fsrc.close()

    fdest = open(destination, "w")
    fdest.write(data)
    fdest.close()


def main():
    if len(sys.argv) != 2:
        print("Usage: python program.py <ExistingFileName>")
        return

    source_file = sys.argv[1]
    dest_file = "Demo.txt"

    if not os.path.exists(source_file):
        print("Source file does not exist")
        return

    CopyFile(source_file, dest_file)
    print(f"Created {dest_file} and copied contents of {source_file} into {dest_file}")


if __name__ == "__main__":
    main()
