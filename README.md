# GPT-Explainer Project

## Overview

GPT-Explainer is a Python script that leverages the GPT-3.5 AI model to explain PowerPoint presentations. It processes .pptx files, sends each slide's text content to the GPT model, and saves the explanations in a JSON file.

## Features

- Parses PowerPoint (.pptx) files to extract text content
- Sends slide content to GPT-3.5-turbo model for explanation
- Processes slides asynchronously for improved performance
- Saves explanations in a JSON file with the same name as the input file
- Implements error handling
- Includes a command-line interface for easy use

## Requirements

- Python 3.7+
- `python-pptx` library for parsing PowerPoint files
- `openai` library for interacting with the OpenAI API
- `asyncio` for asynchronous processing
- OpenAI API key

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/gpt-explainer.git
```
2. Install the required packages:
```
pip install python-pptx openai
```
3. Set up your OpenAI API key as an environment variable or in the `.env` file:
```
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

Run the script from the command line:
python gpt_explainer.py path/to/your/presentation.pptx
Copy
The explanations will be saved in a JSON file with the same name as the input file (e.g., `presentation.json`).

## Implementation Details

- Uses `async/await` syntax with `asyncio` for concurrent processing of slides
- Implements a timeout for API requests to handle potential delays
- Provides informative error messages for slides that fail to process
- Utilizes the `argparse` library for a user-friendly command-line interface

## Future Improvements

- Add support for additional presentation formats
- Implement more advanced error handling and retry mechanisms
- Enhance the prompt engineering for better explanations
- Add options for customizing the output format

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
