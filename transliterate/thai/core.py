from pythainlp.transliterate import transliterate
from pythainlp.tokenize import syllable_tokenize, word_tokenize
from .exceptions import exceptionWords
from .tokenizer import CustomTokenizer

def convert_text_to_ipa(text: str) -> str:
    """
    Convert Thai text to IPA representation.
    
    Args:
        text (str): Input Thai text
        
    Returns:
        str: IPA representation of the input text
    """
    text = ' '.join(text.split())

    custom_tokenizer = CustomTokenizer()
    words = custom_tokenizer.word_tokenize(text)

    ipa_segments = []
    regular_syllables = []
    
    def process_regular_syllables(is_last_syllable: bool, is_word_end: bool):
        if regular_syllables:
            combined = ''.join(regular_syllables).strip()
            print("Regular syllables:", combined)
            if ipa := transliterate(combined, engine='tltk_ipa'):
                ipa_segments.append(ipa)

                if not is_word_end:
                    if not is_last_syllable:
                        ipa_segments.append('.')
                else:
                    ipa_segments.append(' ')
                # if regular_syllables[-1] in words[-1]:  # Check if it's end of word
                #     ipa_segments.append('.')
                # else:
                #     ipa_segments.append(' ')
            regular_syllables.clear()
        
        # print("Current ipa_segments", ipa_segments)

    for word in words:
        print("word: ", word)
        if word == " ":
            process_regular_syllables(is_last_syllable=True, is_word_end=True)

            if ipa_segments and ipa_segments[-1] != ' ':
                ipa_segments.append(' ')
            continue

        syllables = syllable_tokenize(word)
        for i, syllable in enumerate(syllables):
            print("syllable: ", syllable)
            is_first_syllable = i == 0
            is_last_syllable = i == len(syllables) - 1

            if exception_ipa := exceptionWords(syllable):
                process_regular_syllables(is_last_syllable=(not is_last_syllable), is_word_end=is_first_syllable)
                # ipa_segments.extend([exception_ipa, '.'])
                ipa_segments.append(exception_ipa)
                if not is_last_syllable:
                    ipa_segments.append('.')
                elif ipa_segments and ipa_segments[-1] != ' ':
                    ipa_segments.append(' ')
            else:
                regular_syllables.append(syllable)
                # if is_last_syllable:
                #     process_regular_syllables(is_last_syllable=True, is_word_end=True)
                # else:
                #     process_regular_syllables(is_last_syllable=False, is_word_end=False)
        
        # Process syllables at word boundary
        # if not regular_syllables:
        #     if ipa_segments and ipa_segments[-1] == '.':
        #         ipa_segments.pop()
        #     ipa_segments.append(' ')
    
    # Process any remaining syllables
    process_regular_syllables(is_last_syllable=True, is_word_end=True)

    # Remove trailing dot if it exists
    # if ipa_segments and ipa_segments[-1] == '.':
    #     ipa_segments.pop()
    
    # Clean up final result
    result = ' '.join(filter(None, ''.join(ipa_segments).split())).strip()
    return result
    # return ''.join(ipa_segments).strip()