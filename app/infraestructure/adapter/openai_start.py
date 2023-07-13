import openai
import os
import logging


def login_openai() -> dict:
    """
    This is a function for  login to openai.
    """
    logging.warning("Executing login_openai")
    try:
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        openai.api_base = os.environ.get("OPENAI_API_BASE")
        openai.api_type = os.environ.get("OPENAI_API_TYPE")
        openai.api_version = os.environ.get("OPENAI_API_VERSION")

    except Exception as e:
        print("No credentials for openai")
        print(e)
