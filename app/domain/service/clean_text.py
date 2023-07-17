import re


def clean_text(text: str):
    """
    to clean the text
    Args: text
    Returns: text
    """
    text = re.sub(r"\.{2,}", ".", text)
    text = text.replace(r"\n", " ", text)
    # quitar corchetes
    text = text.replace("[", "")
    text = text.replace("]", "")
    # quitar espacios excedentes
    text = re.sub(r"\s+", " ", text)
    return text
