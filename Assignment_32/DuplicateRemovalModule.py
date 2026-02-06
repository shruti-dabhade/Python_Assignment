import os
import hashlib
import logging

def CalculateChecksum(file_path):
    hash_obj = hashlib.md5()
    with open(file_path, "rb") as fobj:
        for block in iter(lambda: fobj.read(4096), b""):
            hash_obj.update(block)
    return hash_obj.hexdigest()

def RemoveDuplicateFiles(directory_name):
    try:
        if not os.path.exists(directory_name):
            logging.error(f"Directory {directory_name} does not exist")
            return

        if not os.path.isdir(directory_name):
            logging.error(f"{directory_name} is not a directory")
            return

        checksum_dict = {}

        for file in os.listdir(directory_name):
            file_path = os.path.join(directory_name, file)

            if os.path.isfile(file_path):
                checksum = CalculateChecksum(file_path)

                if checksum in checksum_dict:
                    os.remove(file_path)
                    logging.info(f"Deleted duplicate file: {file}")
                else:
                    checksum_dict[checksum] = file

    except Exception as e:
        logging.error(f"Error in RemoveDuplicateFiles: {e}")
