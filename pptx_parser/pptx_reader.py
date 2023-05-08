'''
this files contains function to read a PowerPoint file
'''
import pptx

def read_pptx_file(path: str)->list[pptx.slide.Slide]:
    '''
    read a PowerPoint file and return a list of slides
    :param
        path: str, path to the file
    :return:
        list of slides
    '''
    pptx_file = pptx.Presentation(path)
    # Extract the slides from the file
    slides = []
    for slide in pptx_file.slides:
        slides.append(slide)
    return slides

