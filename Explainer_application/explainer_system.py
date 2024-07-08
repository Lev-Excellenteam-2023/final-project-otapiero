import asyncio
import logging
import time
import files_handler.file_handler as fh
from Explainer_application import explain_pptx

UPLOAD_FOLDER = "../files_handler/uploads"
OUTPUT_FOLDER = "../files_handler/outputs"


def process_file(file_name: str):
    """
    Process a file.
    :param file_name: str, name of the file to process.
    :return: None.
    """
    try:

        complete_file_name = UPLOAD_FOLDER + "/" + file_name + ".pptx"
        asyncio.run(explain_pptx(complete_file_name, OUTPUT_FOLDER, file_name))
        print(f"File {file_name} processed successfully")
    except Exception as e:
        print(f"Error processing file {file_name}: {e}")
        logging.debug(f"Error processing file {file_name}: {e}")


def process_files() -> None:
    """
    Process all the files in the 'uploads' folder.
    :return: None.
    """
    logging.debug("Processing files")
    print("Processing files")
    # Get a list of files in the uploads folder
    file_list = fh.get_file_list(folder_name_key="uploads")

    for file_name in file_list:
        # Get the status of the file
        file_status = fh.get_file_status_by_name(file_name)
        if file_status == fh.FileStatus.PENDING:
            print(f"Processing file: {file_name}")
            # Process the file
            process_file(file_name)


def explainer_loop():
    while True:
        process_files()
        time.sleep(10)


if __name__ == "__main__":
    explainer_loop()

