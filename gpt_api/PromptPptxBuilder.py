from typing import List, Dict


class PresentationPromptBuilder:
    """
    A class for building a prompt to ask the GPT API to interpret and explain a PowerPoint presentation.

    Attributes: - prompt (List[Dict[str, str]]): A list of dictionaries representing the prompt, with each dictionary
    representing a slide. - slide_content (List[List[str]]): A list of lists containing the title, text, and notes of
    each slide.

    Methods:
    - build_prompt(): Builds the initial prompt.
    - parse_next_slide(): Parses the next slide from the `slide_content` attribute.
    - update_prompt(response: str): Updates the prompt with the response from the GPT API.
    - get_prompt(): Returns the current prompt.
    """

    def __init__ ( self, slide_content: List[List[str]] ):
        """
        Initializes the `PromptBuilder` instance with a list of slide content.

        :param slide_content: A list of lists containing the title, text, and notes of each slide.
        """
        self.slide_content = slide_content
        self.prompts = self.create_prompt()

    def create_prompt ( self ) -> List[Dict[str, str]]:
        """
        Creates the initial prompt.

        :return: A list of dictionaries representing the prompt.
        """
        prompts = [{
            "role": "system", "content": f"you are a helpful AI that is explaining a PowerPoint presentation."}
        ]
        slides = "".join([f"{slide[0]}{slide[1]}{slide[2]}" for slide in self.slide_content])
        prompts.append({"role": "user", "content": "here is a PowerPoint presentation:" + slides +
                                                   "\nplease explain this slide: " + self.slide_content[0][0] +
                                                   self.slide_content[0][1] + self.slide_content[0][2]})
        self.slide_content.pop(0)
        return prompts

    def get_next_slide ( self ) -> Dict[str, str]:
        """
        Gets the next slide.

        :return: A dictionary representing the next slide.
        """
        if len(self.slide_content) > 0:
            next_slide = self.slide_content.pop(0)
            return {"role": "user", "content": "please explain this slide: " + next_slide[0] + next_slide[1] +
                                               next_slide[2]}
        else:
            return {"role": "system", "content": "No more slides to explain."}

    def update_prompt ( self, response: str ) -> None:
        """
        Updates the prompt with the response from the GPT API and gets the next slide.

        :param response: The response from the GPT API.
        """
        # Update the prompt with the response from the GPT API
        self.prompts.append({"role": "assistant", "content": response})

        # Get the next slide and add it to the prompt
        if len(self.slide_content) > 0:
            self.prompts.append(self.get_next_slide())
        else:
            self.prompts.insert(-1, {"role": "system", "content": "No more slides to explain."})

    def get_prompt(self) -> List[Dict[str, str]]:
        """
        Returns the current prompt.

        :return: A list of dictionaries representing the prompt.
        """
        return self.prompts

    def __iter__(self):
        return self

    def __next__(self):
        """
        Returns the current prompt.
        :return: A list of dictionaries representing the prompt.
        """
        if len(self.slide_content) > 0:
            return self.get_prompt()
        else:
            raise StopIteration

