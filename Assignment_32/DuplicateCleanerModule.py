import os
import hashlib
import logging

def CalculateChecksum(file_path):
    hobj = hashlib.md5()
    with open(file_path, "rb") as f:
        while chunk := f.read(1024):
            hobj.update(chunk)
    return hobj.hexdigest()


def RemoveDuplicateFiles(directory_name):
    try:
        if not os.path.exists(directory_name):
            logging.error("Directory does not exist")
            return

        if not os.path.isdir(directory_name):
            logging.error("Provided path is not a directory")
            return

        checksum_map = {}

        for foldername, subfolders, filenames in os.walk(directory_name):
            for file in filenames:
                file_path = os.path.join(foldername, file)

                checksum = CalculateChecksum(file_path)

                if checksum in checksum_map:
                    os.remove(file_path)
                    logging.info(f"Duplicate deleted: {file_path}")
                else:
                    checksum_map[checksum] = file_path

    except Exception as e:
        logging.error(f"Error in RemoveDuplicateFiles: {e}")
