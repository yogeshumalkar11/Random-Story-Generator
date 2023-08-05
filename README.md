# AI Bedtime Stories Generator with Streamlit

The AI Bedtime Stories Generator is a Python application that uses an AI-powered natural language processing model to generate creative and entertaining bedtime stories for children. It uses an API key for accessing the AI model, which should be provided by the user in the `secret.py` file.

## Requirements

To run this application, you will need to have the following dependencies installed. You can find the specific versions in the `requirements.txt` file.

```plaintext
# requirements.txt
langchain==0.0.252
streamlit==1.25.0
openai==0.27.0
```

## Installation

1. Clone this repository to your local machine.

```bash
git clone https://github.com/yogeshumalkar11/Random-Story-Generator.git
cd Random-Story-Generator
```

2. Set up a virtual environment (optional but recommended).

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies using pip.

```bash
pip install -r requirements.txt
```

4. Obtain an API key for the AI model and put it in the `secret.py` file. You can get the API key from the service provider.

```python
# secret.py
openai_key = "YOUR_API_KEY_HERE"
```

## Usage

The AI Bedtime Stories Generator comes with three files:

1. `story.py`: This module contains the implementation of the AI model and generates the bedtime stories.

2. `secret.py`: You need to put your API key in this file to use the AI model. Please refer to the "Installation" section for details on how to set it up.

3. `main.py`: This is the main script that runs the Streamlit application. It imports the AI model from `story.py` and interacts with the user through a web interface.

To run the application using Streamlit, execute the following command:

```bash
streamlit run main.py
```

This will start a local development server and open the application in your default web browser. Follow the on-screen instructions to input any relevant prompts or information required to generate the story. The AI model will then process the input and generate a bedtime story that you can share with children to make their bedtime magical and enjoyable.

## Note

Please ensure to keep your API key in the `secret.py` file confidential. Avoid sharing it publicly or committing it to version control repositories.

## Contributing

If you have suggestions, bug reports, or want to contribute to this project, please feel free to create issues or submit pull requests.
