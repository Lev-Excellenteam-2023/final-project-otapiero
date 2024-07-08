"""
 this file is used to read a pptx file and extract its slides.
"""

import pptx

def read_pptx_file(path: str)->list[pptx.slide.Slide]:
    """
       Read a PowerPoint file and extract its slides.

       :param path: The path to the PowerPoint file.
       :return: A list of slides in the PowerPoint file.
    """
    pptx_file = pptx.Presentation(path)
    # Extract the slides from the file
    slides = []
    for slide in pptx_file.slides:
        slides.append(slide)
    return slides

