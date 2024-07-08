"""
This module contains functions for reading input from the user.
"""

def set_file_path():
    """
    Set the path to the PowerPoint file.

    :return: str, path to the PowerPoint file.
    """
    file_path = input("Enter the path to the PowerPoint file: ")
    return file_path

def set_folder_response_path():
    """
    Set the path to the folder for the responses.

    :return: str, path to the folder for the responses.
    """
    folder_path = input("Enter the path to the folder for the responses: ")
    return folder_path


def set_api_key ():
    """
    Set the API key.
    :return: str, the API key of openai api.
    """
    api_key = input("Enter the Openai API key: ")
    return api_key