from pythainlp.transliterate import transliterate
from pythainlp.tokenize import syllable_tokenize
from ..utils.punctuations import Punctuations
from .exceptions import exceptionWords
from .tokenizer import CustomTokenizer

# Initialize CustomTokenizer once at module level
_custom_tokenizer = CustomTokenizer()
_punctuations = Punctuations()

def convert_text_to_ipa(text: str, verbose: bool = False) -> str:
    """
    Convert Thai text to IPA representation.
    
    Args:
        text (str): Input Thai text
        
    Returns:
        str: IPA representation of the input text
    """
    text = ' '.join(text.split())

    # Remove all punctuations
    text = _punctuations.remove_punctuations(text)

    # Tokenize text into words
    words = _custom_tokenizer.word_tokenize(text)

    ipa_segments = []
    regular_syllables = []
    
    def process_regular_syllables(is_last_syllable: bool, is_word_end: bool):
        if regular_syllables:
            combined = ''.join(regular_syllables).strip()
            if ipa := transliterate(combined, engine='tltk_ipa'):
                ipa_segments.append(ipa)

                if not is_word_end:
                    if not is_last_syllable:
                        ipa_segments.append('.')
                else:
                    ipa_segments.append(' ')
            regular_syllables.clear()

    for word in words:
        if verbose:
            print("Processing word: ", word)
        if word == " ":
            process_regular_syllables(is_last_syllable=True, is_word_end=True)

            if ipa_segments and ipa_segments[-1] != ' ':
                ipa_segments.append(' ')
            continue

        if ipa := exceptionWords(word):
            process_regular_syllables(is_last_syllable=True, is_word_end=True)
            ipa_segments.append(ipa)
            ipa_segments.append(' ')
            continue

        syllables = syllable_tokenize(word)
        for i, syllable in enumerate(syllables):
            if verbose:
                print("Processing syllable: ", syllable)
            is_first_syllable = i == 0
            is_last_syllable = i == len(syllables) - 1

            if exception_ipa := exceptionWords(syllable):
                process_regular_syllables(is_last_syllable=False, is_word_end=is_first_syllable)
                # ipa_segments.extend([exception_ipa, '.'])
                ipa_segments.append(exception_ipa)
                if not is_last_syllable:
                    ipa_segments.append('.')
                elif ipa_segments and ipa_segments[-1] != ' ':
                    ipa_segments.append(' ')
            else:
                regular_syllables.append(syllable)
    
    # Process any remaining syllables
    process_regular_syllables(is_last_syllable=True, is_word_end=True)
    
    # Clean up final result
    result = ' '.join(filter(None, ''.join(ipa_segments).split())).strip()
    return result