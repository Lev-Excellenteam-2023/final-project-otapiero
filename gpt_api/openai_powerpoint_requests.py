"""
This module contains functions for sending requests for PowerPoint slides to the OpenAI API.
"""

import openai
import logging

from gpt_api.PromptPptxBuilder import PresentationPromptBuilder
from gpt_api.openai_requests import send_request


async def get_powerpoint_explanation(slide_content: str) -> str:
    """
    Send a request to the OpenAI API.

    :param slide_content: The slide  content to explain.
    :return: The response text.
    """
    prompt_builder = PresentationPromptBuilder()
    try:
        prompt = prompt_builder.get_prompt(slide_content)
        response = await send_request(prompt)
        return response
    except openai.OpenAIError as e:
        logging.error(f"OpenAI API Error: {str(e)}")
        raise

