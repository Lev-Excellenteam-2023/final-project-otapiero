# Initialize the OpenAI API when the package is imported
from gpt_api.openai_requests import init_openai_api
from dotenv import load_dotenv

load_dotenv()

init_openai_api()


