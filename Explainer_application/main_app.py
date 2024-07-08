import asyncio
import logging
import os
import argparse
import sys

from Explainer_application.gpt_api.openai_powerpoint_requests import get_powerpoint_explanation
from Explainer_application.json_outpout.json_file_writer import save_content_to_json_file
from Explainer_application.pptx_parser.slide_text_extractor import SlideTextExtractor
# Add current directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
import input_util


async def cli_main():
    """
    Asynchronous function to run the main program from the command line.

    Raises:
        Exception: If an error occurs during the processing.
    """
    try:
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('pptx_file', nargs='?', default=None, help='Path to the PowerPoint file')
        parser.add_argument('output_folder', nargs='?', default=None, help='Path to the output folder')
        args = parser.parse_args()
        pptx_file_path = args.pptx_file or input_util.set_file_path()
        folder_result_path = args.output_folder or input_util.set_folder_response_path()
        file_name = os.path.splitext(os.path.basename(pptx_file_path))[0]
        await explain_pptx(pptx_file_path, folder_result_path, file_name)
    except Exception as e:
        logging.error(f"Error: {str(e)}")


async def explain_pptx(pptx_file_path: str, folder_result_path: str, file_name: str):
    """
    Process a PowerPoint file and extract explanations for each slide.

    :param pptx_file_path: Path to the PowerPoint file.
    :param folder_result_path: Path to the output folder.
    :param file_name: Name of the PowerPoint file.
    """
    try:
        slide_text_extractor = SlideTextExtractor(pptx_file_path)

        coroutines = (get_powerpoint_explanation(slide) for slide in slide_text_extractor)
        responses = await asyncio.gather(*coroutines)

        save_content_to_json_file(folder_result_path, file_name, list(responses))
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise e


def main():
    """
    Entry point of the script.

    It calls the `cli_main` function to process the PowerPoint file and handle any exceptions that may occur.

    """
    try:
        asyncio.run(cli_main())
    except Exception as e:
        logging.error(f"Error: {str(e)}")

if __name__ == '__main__':
    main()
