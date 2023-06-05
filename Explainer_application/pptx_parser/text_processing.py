"""
 this file is used to process the text in the pptx file
"""
from typing import List


def process_pptx_slide_content(pptx_slide_content: List[str]) -> str:
    """
    process text from a pptx file content to make it ready for analysis.

    :param pptx_slide_content: list of one slide content,title, text and notes.
    :return: str, processed text.
    """

    slide_title = process_text(pptx_slide_content[0])
    slide_text = process_text(pptx_slide_content[1])
    slide_notes = process_text(pptx_slide_content[2])
    slide_content = "Slide Title: " + slide_title + "\n" + "Slide Text: " + slide_text + "\n" + \
                    "Slide Notes: " + slide_notes + "\n"
    return slide_content


def process_text(text: str) -> str:
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
