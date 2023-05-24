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


'''
import openai

from gpt_api.PromptPptxBuilder import PresentationPromptBuilder
from pptx_parser.slide_text_extractor import get_pptx_file_content

pptx_file_path = r"C:\\Users\\ouriel\\Desktop\\End of course exercise - kickof - upload.pptx"
pptx_file_content = get_pptx_file_content(pptx_file_path)
print("---------------------------------------------------------------------")
prompt = PresentationPromptBuilder(pptx_file_content)
message = prompt.get_prompts()
openai.api_key = "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"

response =openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=message)

response_text = response['choices'][0]['message']['content']
print(response_text)
prompt.update_prompt(response_text)
message = prompt.get_prompts()
print('---------------------------------------------------------------------')
print(message)
response =openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message)
response_text = response['choices'][0]['message']['content']
print(response_text)'''
