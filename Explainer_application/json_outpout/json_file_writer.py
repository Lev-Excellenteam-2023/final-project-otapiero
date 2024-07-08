import json
import os
from typing import List


def create_json_file(json_file_path: str, file_name: str) -> str:
    """
    Create an empty JSON file at the given path with the given name, or with a new name if the file already exists.

        :param json_file_path: The path where the file should be created.
        :param file_name: The name of the file.
        :return: The path of the created file.
    """
    if not os.path.isdir(json_file_path):
        raise NotADirectoryError(f"'{json_file_path}' is not a directory.")
    file_path = os.path.join(json_file_path, f"{file_name}.json")
    if os.path.exists(file_path):
        # if file already exists, create a new file with a different name
        i = 1
        while True:
            new_file_path = os.path.join(json_file_path, f"{file_name} ({i}).json")
            if not os.path.exists(new_file_path):
                file_path = new_file_path
                break
            i += 1
    try:
        with open(file_path, "w") as json_file:
            json_file.write("{}")
    except OSError as e:
        raise OSError(f"Invalid file path: '{file_path}' ({e})")

    print(f"File '{os.path.basename(file_path)}' created successfully.")
    return file_path


def save_content_to_json_file(json_file_path: str, file_name: str, list_content: List[List[str]]) -> None:
    """
    Save a list of lists containing strings to a JSON file at the given path with the given name.

        :param json_file_path: The path where the file should be saved.
        :param file_name: The name of the file.
        :param list_content: The content to be saved in the file as a list of lists containing strings.
        :return: None.
    """
    try:
        file_path = create_json_file(json_file_path, file_name)
    except OSError as e:
        raise OSError(f"Invalid file path: '{json_file_path}' ({e})")

    with open(file_path, "w") as json_file:
        json.dump(list_content, json_file, indent=2)

    print(f"Content saved successfully to '{file_name}.json'.")


if __name__ == "__main__":
    import Explainer_application.pptx_parser.slide_text_extractor as slide_text_extractor

    pptx_file_path = r"C:\Users\ouriel\Desktop\End of course exercise - kickof - upload.pptx"
    slide_extractor = slide_text_extractor.SlideTextExtractor(pptx_file_path=pptx_file_path)
    pptx_file_content = [slide for slide in slide_extractor]
    # save content to json file
    save_content_to_json_file(r"C:\Users\ouriel\Desktop", "end of course exercise kickof upload", pptx_file_content)
