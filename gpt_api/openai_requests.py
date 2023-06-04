from typing import Dict, List

import openai
import os
import logging

from app import input_util

"""
This file is used to send requests to the openai api. 
"""


async def send_request(prompt:  List[Dict[str, str]]) -> str:
    """
    Send a request to the OpenAI API.

    :param prompt: The prompt to send.
    :return: The response text.
    """
    try:
        print(prompt)
        response =  openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt
        )
        logging.info(response['usage']['total_tokens'])
        print(response['usage']['total_tokens'])
        return extract_response(response)
    except openai.OpenAIError as e:
        logging.error(f"OpenAI API Error: {str(e)}")
        raise


def extract_response(response: Dict) -> str:
    """
    Extract the response text from the response dictionary.

    :param response: The response dictionary.
    :return: The response text.
    """
    print("response: "+response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']



def init_openai_api():
    """
    Initialize the OpenAI API.
    """
    if 'OPENAI_API_KEY' in os.environ:
        openai.api_key = os.environ.get('OPENAI_API_KEY', "")
    else:
        openai.api_key = input_util.set_api_key()


