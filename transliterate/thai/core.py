from typing import List
from pythainlp.transliterate import transliterate
from .exceptions import exceptionWords

def convert_text_to_ipa(text: str) -> str:
    """
    Convert Thai text to IPA representation.
    
    Args:
        text (str): Input Thai text
        
    Returns:
        str: IPA representation of the input text
    """
    texts = text.split()
    ipa = ''
    for i, text in enumerate(texts):
        seg = transliterate(text, engine='tltk_ipa')
        if seg == '' or seg[-1] == '.':
            seg = exceptionWords(text)
        ipa += seg
        if i != len(texts) - 1:
            ipa += ' '
    return ipa