from typing import List
from ..thai.core import convert_text_to_ipa
from ..utils.phoneme_converter import convert_ipa_to_phonemes
from .base_phonemizer import BasePhonemizer
from ..utils.punctuations import Punctuations

class ThaiPhonemizer(BasePhonemizer):
    """Phonemizer for Thai text."""
    
    def phonemize(self, text: str, strip: bool = True) -> List[str]:
        """Convert Thai text to phonemes."""

        try:
            if strip:
                text = text.strip()

            # Remove all punctuations
            text = Punctuations().remove_punctuations(text)
            
            if not text:
                return []
                
            # Convert to IPA first
            ipa = convert_text_to_ipa(text)
            if not ipa:
                return []

            return convert_ipa_to_phonemes(ipa)
        except Exception as e:
            raise ValueError(f"Failed to phonemize Thai text {text}: {str(e)}")
