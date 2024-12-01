"""
This module provides functions to interact with different AI models
including Anthropic, Gemini, and OpenAI.
"""

import os
from dotenv import load_dotenv
import anthropic
import google.generativeai as genai
from openai import OpenAI

load_dotenv()

# Anthropic model
anthropic_client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
ANTHROPIC_MODEL = "claude-3-5-haiku-latest"
# ANTHROPIC_MODEL = "claude-3-5-sonnet-latest"

# Gemini model
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
gemini_generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
GEMINI_MODEL = "gemini-1.5-flash"
# GEMINI_MODEL = "gemini-1.5-pro"

# OpenAI model
openai_client = OpenAI()
OPENAI_MODEL = "gpt-4o-mini"
# OPENAI_MODEL = "gpt-4o"


def ask_anthropic(prompt, model=ANTHROPIC_MODEL):
    """
    Sends a prompt to the Anthropic model and returns the response.

    Args:
        prompt (str): The prompt to send to the model.
        model (str): The model to use for generating the response.

    Returns:
        str: The generated response from the model.
    """
    message = anthropic_client.messages.create(
        model=model,
        max_tokens=1024,
        temperature=0.05,  # Adding a small amount of randomness
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def ask_gemini(prompt, model_name=GEMINI_MODEL):
    """
    Sends a prompt to the Gemini model and returns the response.

    Args:
        prompt (str): The prompt to send to the model.
        model_name (str): The model to use for generating the response.

    Returns:
        str: The generated response from the model.
    """
    gemini_model_instance = genai.GenerativeModel(
        model_name=model_name, generation_config=gemini_generation_config
    )
    response = gemini_model_instance.generate_content(prompt)
    return response.text


def ask_openai(prompt, model=OPENAI_MODEL):
    """
    Sends a prompt to the OpenAI API and returns the response.

    Args:
      prompt (str): The input text to be sent to the OpenAI API.
      model (str, optional): The model to use for generating the response.
                             Defaults to OPENAI_MODEL.

    Returns:
      str: The content of the response from the OpenAI API.
    """
    completion = openai_client.chat.completions.create(
        model=model,
        temperature=0.0,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )
    return completion.choices[0].message.content
