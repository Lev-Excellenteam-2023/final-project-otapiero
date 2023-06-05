from typing import List, Dict


class PresentationPromptBuilder:
    """
    A class for building a prompt to ask the GPT API to interpret and explain a PowerPoint presentation.

    Attributes:
        prompt (List[Dict[str, str]]): A list of dictionaries representing the prompt, with each dictionary
            representing a slide.

    Methods:
        __init__(): Initializes the PresentationPromptBuilder class.
        create_initial_prompt(): Creates the initial prompt.
        update_prompt(slide_content: str) -> None: Updates the prompt with the slide content.
        get_prompt(slide_content: str) -> List[Dict[str, str]]: Updates and return the prompt.
    """

    def __init__(self):
        """
        Initializes the PresentationPromptBuilder class.
        """
        self.prompt = []
        self.create_initial_prompt()

    def create_initial_prompt(self):
        """
        Creates the initial prompt.

        :return: None
        """
        prompt = [
            {
                "role": "system",
                "content": "you are a helpful AI that is explaining a PowerPoint presentation. Note: "
                           "your responses should only contain the explanation of the slide."
            },
            {
                "role": "user",
                "content": ""
            }
        ]
        self.prompt = prompt

    def update_prompt(self, slide_content: str) -> None:
        """
        Updates the prompt with the slide content.

        :param slide_content: The slide content to add to the prompt.
        :return: None
        """
        self.prompt[-1]["content"] = "here is a slide from a PowerPoint presentation: please explain this slide: " + \
                                     slide_content

    def get_prompt(self, slide_content: str) -> List[Dict[str, str]]:
        """
        Returns the current prompt.

        :param slide_content: The slide content to add to the prompt.
        :return: A list of dictionaries representing the prompt.
        """
        self.update_prompt(slide_content)
        return self.prompt
