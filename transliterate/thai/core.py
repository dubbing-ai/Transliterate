from typing import List
from pythainlp.transliterate import transliterate
from pythainlp.tokenize import syllable_tokenize, word_tokenize
from .exceptions import exceptionWords

def convert_text_to_ipa(text: str) -> str:
    """
    Convert Thai text to IPA representation.
    
    Args:
        text (str): Input Thai text
        
    Returns:
        str: IPA representation of the input text
    """
    texts = word_tokenize(text)
    ipa_segments = []
    
    for text in texts:
        # Split text into syllables
        syllables = syllable_tokenize(text)
        
        for syllable in syllables:
            # Check for exception words first
            ipa_segment = exceptionWords(syllable)
            
            if not ipa_segment:
                # If no exception, use transliteration
                ipa_segment = transliterate(syllable, engine='tltk_ipa') or exceptionWords(syllable)
            
            if ipa_segment:
                ipa_segments.append(ipa_segment)
                ipa_segments.append('.')

        if ipa_segments and ipa_segments[-1] == '.':
            ipa_segments.pop()

        ipa_segments.append(' ')
    
    # Join the segments into a final string
    ipa = ''.join(ipa_segments).strip()
    return ipa