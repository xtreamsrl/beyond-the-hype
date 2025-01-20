"""Contains miscellanea utility functions."""

import os

from dotenv import load_dotenv


def get_openai_api_key(api_key: str | None = None) -> str:
    """Get the OpenAI API key from the environment or as an argument.

    Args:
        api_key: OpenAI API key.

    Returns:
        OpenAI API key.
    """
    load_dotenv()

    if api_key:
        return api_key

    oai_api_key = os.getenv("OPENAI_API_KEY")
    if oai_api_key:
        return oai_api_key

    msg = (
        "No OpenAI API key found. "
        "Please set it in the environment variable OPENAI_API_KEY "
        "or pass it as an argument."
    )
    raise ValueError(msg)
