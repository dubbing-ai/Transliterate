from typing import List
from .vowels import Vowels

vowels = Vowels()

def convert_ipa_to_phonemes(ipa_phoneme: str) -> List[str]:
    """
    Convert IPA representation to phoneme list.
    
    Args:
        ipa_phoneme (str): IPA string representation
        
    Returns:
        List[str]: List of phonemes
    """
    phoneme_list = []
    for word in ipa_phoneme.split():
        for phn in word.split('.'):
            tone, other_phn = phn[-1], phn[:-1]
            if tone == '1':
                tone = ''

            found_vowel = ''
            for vowel in vowels.all_vowels:
                if vowel in other_phn:
                    found_vowel = vowel
                    break

            initial_consonant, final_consonant = other_phn.split(found_vowel)

            if initial_consonant:
                phoneme_list.append(initial_consonant)
            if found_vowel:
                phoneme_list.append(f'{found_vowel}{tone}')
            if final_consonant:
                phoneme_list.append(final_consonant)

        phoneme_list.append('_')

    if phoneme_list and phoneme_list[-1] == '_':
        phoneme_list.pop()
    return phoneme_list