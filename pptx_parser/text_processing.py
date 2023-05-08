"""
 this file is used to process the text in the pptx file
"""


def process_pptx_file_content ( pptx_file_content: list[list[str, str, str]] ) -> list[list[str]]:
    """
    process text from a pptx file content to make it ready for analysis.

    :param pptx_file_content: list of lists, each list contains title, text and notes of a slide.
    :return: list of lists, each list contains title, text and notes of a slide as one string.
    """
    processed_pptx_file_content = []
    for slide in pptx_file_content:
        if slide[0] == "" and slide[1] == "" and slide[2] == "":
            continue
        slide_title = process_text(slide[0])
        slide_text = process_text(slide[1])
        slide_notes = process_text(slide[2])
        slide_content = ["Slide Title: " + slide_title + "\n", "Slide Text: " + slide_text + "\n",
                         "Slide Notes: " + slide_notes + "\n"]
        processed_pptx_file_content.append(slide_content)

    return processed_pptx_file_content


def process_text ( text: str ) -> str:
    """
    process text to make it ready for analysis.

    :param text: str, text to be processed.
    :return:
        str, processed text.
    """
    # Remove extra spaces
    text = text.split()
    text = ' '.join(text)

    # Remove special characters
    special_chars = ['\n', '\t', '\r', '\f', '\v']
    text = ''.join([c for c in text if c not in special_chars])
    return text
