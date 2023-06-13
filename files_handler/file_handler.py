"""
This module is used to handle files.

"""
import os

from files_handler.FileStatus import FileStatus

FILE_UPLOADS_PATH = "uploads"
FILE_OUTPUT_PATH = "outputs"


def save_file(file_name: str, file_content: bytes, folder_name: str = FILE_UPLOADS_PATH):
    """
    Save a file in the file storage.
    :param folder_name:
    :param file_name: str, name of the file.
    :param file_content: bytes, content of the file.
    :return: None.
    """
    try:
        # check if the file storage path exists
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        # save the file if the file does not exist
        if not os.path.exists(os.path.join(folder_name, file_name)):
            with open(os.path.join(folder_name, file_name), "wb") as f:
                f.write(file_content)
    except OSError as e:
        raise OSError(f"Invalid file path: '{file_name}' ({e})")


def get_file(file_name: str, folder_name: str = FILE_OUTPUT_PATH) -> bytes:
    """
    Get a file from the file storage.
    :param folder_name: str, name of the folder.
    :param file_name: str, name of the file.
    :return: bytes, content of the file.
    """
    try:
        with open(os.path.join(folder_name, file_name), "rb") as f:
            return f.read()
    except OSError as e:
        raise OSError(f"Invalid file path: '{file_name}' ({e})")


def file_exist(file_name: str, folder_name: str = FILE_OUTPUT_PATH) -> bool:
    if os.path.exists(os.path.join(folder_name, file_name)):
        return True
    return False


def get_file_status(file_name: str) -> FileStatus:
    """
    Get the status of the file.
    :param file_name: str, name of the file.
    :return: FileStatus, status of the file.
    """
    try:
        # if the file do not exist in uploads folder, return NOT_FOUND
        if not file_exist(file_name, folder_name=FILE_UPLOADS_PATH):
            return FileStatus.NOT_FOUND
        # if the file do not exist in outputs folder, return PENDING
        if not file_exist(file_name, folder_name=FILE_OUTPUT_PATH):
            return FileStatus.PENDING
        # if the file exist in outputs folder, return DONE
        return FileStatus.DONE
    except OSError as e:
        raise OSError(f"Invalid file path: '{file_name}' ({e})")
