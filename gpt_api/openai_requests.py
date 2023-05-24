from typing import Dict, List

import openai
import os
import logging

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
        response = await openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt
        )
        logging.info(response['usage']['total_tokens'])
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
    return response['choices'][0]['text']


def init_openai_api():
    """
    Initialize the OpenAI API.
    """
    openai.api_key = os.environ.get('OPENAI_API_KEY', "")
