import datetime

import files_handler.file_handler as fh


def create_file(uid: str, file_name: str, file_content: bytes) -> bool:
    """
    Create a file in the file storage.
    :param uid: str, uuid of the file.
    :param file_name: str, name of the file.
    :param file_content: bytes, content of the file.
    :return: bool, True if the file is created successfully, False otherwise.
    """
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    new_filename = f"{file_name}_{timestamp}_{uid}"

    try:
        if not fh.file_exist(new_filename):
            fh.save_file(new_filename, file_content)
            return True
    except OSError as e:
        raise OSError(f"Invalid file path: '{file_name}' ({e})")
    return False


