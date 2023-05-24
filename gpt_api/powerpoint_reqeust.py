"""
 This file is used to send requests for PowerPoint files to the openai api.
"""
from typing import List, Dict

import openai
import logging

from gpt_api.PromptPptxBuilder import PresentationPromptBuilder
from gpt_api.openai_requests import send_request


async def get_powerpoint_explanation(powerpoint_file_content: List[List[str]]) -> List[Dict[str, str]]:
    """
    Send a request to the OpenAI API.

    :param powerpoint_file_content: The PowerPoint file content to send.
    :return: The response text.
    """
    prompt_builder = PresentationPromptBuilder(powerpoint_file_content)
    try:
        for prompt in prompt_builder:
            response = await send_request(prompt)
            prompt_builder.update_prompt(response)
    except openai.OpenAIError as e:
        logging.error(f"OpenAI API Error: {str(e)}")
        raise
    return prompt_builder.get_prompt()




















'''
import openai

from gpt_api.PromptPptxBuilder import PresentationPromptBuilder
from pptx_parser.slide_text_extractor import get_pptx_file_content

pptx_file_path = r"C:\Users\ouriel\Desktop\End of course exercise - kickof - upload.pptx"
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