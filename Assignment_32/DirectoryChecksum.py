"""Please follow below rules while designing automation script as  
• Accept input through command line or through file. 
• Display any message in log file instead of console. 
• For separate task define separate function. 
• For robustness handle every expected exception. 
• Perform validations before taking any action. 
• Create user defined modules to store the functionality. 
1.Design automation script which accept directory name and display checksum of all files. 
Usage : DirectoryChecksum.py “Demo” 
Demo is name of directory."""


import sys
import logging
from ChecksumModule import DisplayChecksums

def main():
    try:
        logging.basicConfig(
            filename="DirectoryChecksum.log",
            level=logging.INFO,
            format="%(asctime)s : %(levelname)s : %(message)s"
        )

        if len(sys.argv) != 2:
            logging.error("Invalid arguments")
            logging.info("Usage: DirectoryChecksum.py <DirectoryName>")
            return

        directory_name = sys.argv[1]

        DisplayChecksums(directory_name)

    except Exception as e:
        logging.error(f"Exception in main: {e}")

if __name__ == "__main__":
    main()
