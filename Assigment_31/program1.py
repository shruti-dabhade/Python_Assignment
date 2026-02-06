"""Please follow below rules while designing automation script as  
• Accept input through command line or through file. 
• Display any message in log file instead of console. 
• For separate task define separate function. 
• For robustness handle every expected exception. 
• Perform validations before taking any action. 
• Create user defined modules to store the functionality.

.Design automation script which accept directory name and file extension from user. Display all 
files with that extension. 
Usage : DirectoryFileSearch.py “Demo” “.txt” 
Demo is name of directory and .txt is the extension that we want to search.

"""


import sys
import logging
from FileSearchModule import DisplayFilesByExtension

def main():
    try:
        # Log configuration
        logging.basicConfig(
            filename="DirectoryFileSearch.log",
            level=logging.INFO,
            format="%(asctime)s : %(levelname)s : %(message)s"
        )

        # Command line argument validation
        if len(sys.argv) != 3:
            logging.error("Invalid number of arguments")
            logging.info("Usage: DirectoryFileSearch.py <DirectoryName> <Extension>")
            return

        directory_name = sys.argv[1]
        extension = sys.argv[2]

        DisplayFilesByExtension(directory_name, extension)

    except Exception as e:
        logging.error(f"Exception in main: {e}")

if __name__ == "__main__":
    main()
