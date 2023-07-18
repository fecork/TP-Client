import re


def clean_text(text: str):
    """
    to clean the text
    Args: text
    Returns: text
    """
    text = re.sub(r"\.{2,}", ".", text)
    text = text.replace("\n", " ")
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = re.sub(r"\s+", " ", text)
    return text
