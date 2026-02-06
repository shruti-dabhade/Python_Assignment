import os
import logging

def DisplayFilesByExtension(directory_name, extension):
    try:
        # Validation
        if not os.path.exists(directory_name):
            logging.error("Directory does not exist")
            return

        if not os.path.isdir(directory_name):
            logging.error("Provided path is not a directory")
            return

        logging.info(f"Searching for files with extension {extension} in {directory_name}")

        found = False
        for file in os.listdir(directory_name):
            if file.endswith(extension):
                logging.info(file)
                found = True

        if not found:
            logging.info("No files found with given extension")

    except PermissionError:
        logging.error("Permission denied while accessing directory")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
