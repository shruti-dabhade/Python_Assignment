import sys
import logging
from CopyExtModule import CopyFilesByExtension

def main():
    try:
        logging.basicConfig(
            filename="DirectoryCopyExt.log",
            level=logging.INFO,
            format="%(asctime)s : %(levelname)s : %(message)s"
        )

        if len(sys.argv) != 4:
            logging.error("Invalid arguments")
            logging.info("Usage: DirectoryCopyExt.py <SourceDir> <DestDir> <Extension>")
            return

        source_dir = sys.argv[1]
        dest_dir = sys.argv[2]
        extension = sys.argv[3]

        CopyFilesByExtension(source_dir, dest_dir, extension)

    except Exception as e:
        logging.error(f"Exception in main: {e}")

if __name__ == "__main__":
    main()
