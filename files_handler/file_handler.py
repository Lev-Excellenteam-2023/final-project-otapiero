"""
This module is used to handle files.

"""
import json
import os
from typing import List
import io
from pptx import Presentation


from files_handler.FileStatus import FileStatus

FILE_UPLOADS_PATH = "uploads"
FILE_OUTPUT_PATH = "outputs"


def save_file(file_name: str, file_content: bytes,file_type: str = "pptx", folder_name: str = FILE_UPLOADS_PATH):
    """
    Save a file in the file storage.
    :param file_type: str, type of the file.
    :param folder_name: str, name of the folder.
    :param file_name: str, name of the file.
    :param file_content: bytes, content of the file.
    :return: None.
    """
    try:
        # check if the file storage path exists
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        # save the file if the file does not exist
        if not file_exist(file_name=file_name, folder_name=folder_name):
            if file_type == "pptx":
                prs = Presentation(io.BytesIO(file_content))
                prs.save(os.path.join(folder_name, file_name+"."+file_type))
            elif file_type == "json":
                json_data = json.loads(file_content.decode("utf-8"))
                with open(os.path.join(folder_name, file_name+"."+file_type), 'w') as outfile:
                    json.dump(json_data, outfile, indent=4)
            else:
                raise ValueError(f"Invalid file type: '{file_type}'")
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
        if not file_uid_exist(file_name, folder_name=FILE_UPLOADS_PATH):
            return FileStatus.NOT_FOUND
        # if the file do not exist in outputs folder, return PENDING
        if not file_uid_exist(file_name, folder_name=FILE_OUTPUT_PATH):
            return FileStatus.PENDING
        # if the file exist in outputs folder, return DONE
        return FileStatus.DONE
    except OSError as e:
        raise OSError(f"Invalid file path: '{file_name}' ({e})")


def get_file_list(folder_name: str = FILE_UPLOADS_PATH) -> List[str]:
    """
    Get the list of files in the folder.
    :param folder_name: str, name of the folder.
    :return: list, list of files without the type.
    """
    try:
        return [file_name.split(".")[0] for file_name in os.listdir(folder_name)]
    except OSError as e:
        raise OSError(f"Invalid folder path: '{folder_name}' ({e})")


def delete_file(file_name: str, folder_name: str = FILE_UPLOADS_PATH):
    """
    Delete a file from the file storage.
    :param folder_name: str, name of the folder.
    :param file_name: str, name of the file to delete without the type.
    :return: None.
    """
    try:
        # delete the file if the file exist
        if file_exist(file_name=file_name, folder_name=folder_name):
            [os.remove(os.path.join(folder_name, file)) for file in os.listdir(folder_name)
             if file_name == file.split(".")[0]]
    except OSError as e:
        raise OSError(f"Invalid file path: '{file_name}' ({e})")


def file_uid_exist(uid: str, folder_name: str = FILE_UPLOADS_PATH) -> bool:
    """
    Check if a file with the uid exist in the folder.
    :param folder_name: str, name of the folder.
    :param uid: str, uid of the file.
    :return: bool, True if the file exist, False otherwise.
    """
    try:
        for file_name in get_file_list(folder_name):
            if uid == file_name.split("_")[-1].split(".")[0]:
                return True
        return False
    except OSError as e:
        raise OSError(f"Invalid folder path: '{folder_name}' ({e})")


def get_file_name(uid: str, folder_name: str = FILE_UPLOADS_PATH) -> str:
    """
    Get the file name from the uid.
    :param folder_name: str, name of the folder.
    :param uid: str, uid of the file.
    :return: str, name of the file.
    """
    try:
        for file_name in get_file_list(folder_name):
            if uid == file_name.split("_")[-1]:
                return file_name
        return ""
    except OSError as e:
        raise OSError(f"Invalid folder path: '{folder_name}' ({e})")