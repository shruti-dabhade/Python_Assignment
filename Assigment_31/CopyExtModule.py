import os
import shutil
import logging

def CopyFilesByExtension(source_dir, dest_dir, extension):
    try:
        if not os.path.exists(source_dir):
            logging.error(f"Source directory {source_dir} does not exist")
            return

        if not os.path.isdir(source_dir):
            logging.error(f"{source_dir} is not a directory")
            return

        if not os.path.exists(dest_dir):
            os.mkdir(dest_dir)
            logging.info(f"Created directory {dest_dir}")

        for file in os.listdir(source_dir):
            if file.endswith(extension):
                src_path = os.path.join(source_dir, file)
                dest_path = os.path.join(dest_dir, file)

                if os.path.isfile(src_path):
                    shutil.copy(src_path, dest_path)
                    logging.info(f"Copied {file}")

    except Exception as e:
        logging.error(f"Error in CopyFilesByExtension: {e}")
