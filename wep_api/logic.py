import datetime
import json
from typing import Dict

import files_handler.file_handler as fh
from files_handler.FileStatus import FileStatus
from uuid_handler import is_valid_uid

def create_file(uid: str, file_name: str, file_content: bytes):
    """
    Create a file in the file storage.
    :param uid: str, uuid of the file.
    :param file_name: str, name of the file.
    :param file_content: bytes, content of the file.
    :return: None.
    """
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    new_filename = f"{file_name}_{timestamp}_{uid}"

    try:
        if not fh.file_exist(new_filename):
            fh.save_file(new_filename, file_content)
            return True
        else:
            raise FileExistsError(f"File '{new_filename}' already exists.")
    except OSError as e:
        raise OSError(f"Invalid file path: '{file_name}' ({e})")


def get_file_status(uid: str) -> FileStatus:
    """
    Get the status of the file.
    :param uid: str, uuid of the file.
    :return: FileStatus, status of the file.
    """
    try:
        status = fh.get_file_status(uid)
        return status
    except OSError as e:
        raise OSError(f"Invalid file path: '{uid}' ({e})")


def get_original_file_name(file_name : str) -> str:
    """
    Get the original file name from the file name.
    :param file_name: str, name of the file.
    :return: str, original file name.
    """
    return "_".join(file_name.split("_")[:-1])
def get_timestamp(file_name : str) -> str:
    """
    Get the timestamp from the file name.
    :param file_name: str, name of the file.
    :return: str, timestamp.
    """
    return file_name.split("_")[-2]

def create_response(uid: str) -> Dict[str, str]:
    """
    Create a response for the API.
    :param uid: str, uuid of the file.
    :return: Dict[str, str], response for the API.
    """
    try:
        if not is_valid_uid(uid):
            raise FileNotFoundError(f"File '{uid}' not found.")
        status = get_file_status(uid)
        file_name = fh.get_file_name(uid)
        if status == FileStatus.DONE:
            file_response = json.dumps(fh.get_file(uid).decode("utf-8"))
            return {"status": "done", "filename": get_original_file_name(file_name),
                    "timestamp": get_timestamp(file_name), "explanation": file_response}

        elif status == FileStatus.PENDING:
            return {"status": "pending", "filename": get_original_file_name(file_name),
                    "timestamp": get_timestamp(file_name), "explanation": None}
        elif status == FileStatus.NOT_FOUND:
            raise FileNotFoundError(f"File '{uid}' not found.")
    except OSError as e:
        raise OSError(f"Invalid file path: '{uid}' ({e})")