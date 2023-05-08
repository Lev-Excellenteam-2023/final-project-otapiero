'''
  this file is used to write in json file
'''
import json
import pptx_parser.slide_text_extractor as slide_text_extractor

def create_json_file(json_file_path: str, file_name: str) -> None:
    """
    Create an empty JSON file at the given path with the given name.

    :param json_file_path: The path where the file should be created.
    :param file_name: The name of the file.
    """
    with open(f"{json_file_path}/{file_name}.json", "w") as json_file:
        json_file.write("{}")

    print(f"File '{file_name}.json' created successfully.")


def save_content_to_json_file(json_file_path: str, file_name: str, file_content: list[list[str]]) -> None:
    """
    Save a list of lists containing strings to a JSON file at the given path with the given name.

    :param json_file_path: The path where the file should be saved.
    :param file_name: The name of the file.
    :param file_content: The content to be saved in the file.
    """
    create_json_file(json_file_path, file_name)

    with open(f"{json_file_path}/{file_name}.json", "w") as json_file:
        json.dump(file_content, json_file)

    print(f"Content saved successfully to '{file_name}.json'.")



if __name__ == "__main__":
    pptx_file_path = r"C:\Users\ouriel\Desktop\End of course exercise - kickof - upload.pptx"
    pptx_file_content = slide_text_extractor.get_pptx_file_content(pptx_file_path)
    # save content to json file

    save_content_to_json_file(r"C:\Users\ouriel\Desktop", "pptx_file_content", pptx_file_content)