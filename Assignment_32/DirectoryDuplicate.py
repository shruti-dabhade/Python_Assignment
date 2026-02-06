""". Design automation script which accept directory name and write names of duplicate files from 
that directory into log file named as Log.txt. Log.txt file should be created into current 
directory. 
Usage : DirectoryDusplicate.py “Demo” 
Demo is name of directory. """

import sys
import logging
from DuplicateModule import FindDuplicateFiles

def main():
    try:
        logging.basicConfig(
            filename="Log.txt",
            level=logging.INFO,
            format="%(asctime)s : %(levelname)s : %(message)s"
        )

        if len(sys.argv) != 2:
            logging.error("Invalid arguments")
            logging.info("Usage: DirectoryDuplicate.py <DirectoryName>")
            return

        directory_name = sys.argv[1]

        FindDuplicateFiles(directory_name)

    except Exception as e:
        logging.error(f"Exception in main: {e}")

if __name__ == "__main__":
    main()
