from typing import List
from ..thai.core import convert_text_to_ipa
from ..utils.phoneme_converter import convert_ipa_to_phonemes
from .base_tokenizer import BaseTokenizer
from ..utils.punctuations import Punctuations

class ThaiTokenizer(BaseTokenizer):
    """Tokenizer for Thai text."""
    
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
            raise ValueError(f"Failed to phonemize Thai text: {str(e)}")
