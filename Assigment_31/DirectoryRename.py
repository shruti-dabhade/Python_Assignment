""" Design automation script which accept directory name and two file extensions from user. 
Rename all files with first file extension with the second file extenntion. 
Usage : DirectoryRename.py “Demo” “.txt” “.doc” 
Demo is name of directory and .txt is the extension that we want to search and rename 
with .doc. 
After execution this script each .txt file gets renamed as .doc."""


import sys
import logging
from RenameModule import RenameFiles

def main():
    try:
        logging.basicConfig(
            filename="DirectoryRename.log",
            level=logging.INFO,
            format="%(asctime)s : %(levelname)s : %(message)s"
        )

        if len(sys.argv) != 4:
            logging.error("Invalid arguments")
            logging.info("Usage: DirectoryRename.py <Directory> <OldExt> <NewExt>")
            return

        directory_name = sys.argv[1]
        old_ext = sys.argv[2]
        new_ext = sys.argv[3]

        RenameFiles(directory_name, old_ext, new_ext)

    except Exception as e:
        logging.error(f"Exception in main: {e}")

if __name__ == "__main__":
    main()
