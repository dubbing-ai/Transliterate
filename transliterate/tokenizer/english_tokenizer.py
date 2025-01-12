import re
from typing import List, Union, Pattern
from phonemizer.backend import EspeakBackend
from phonemizer.backend.espeak.language_switch import LanguageSwitch
from phonemizer.backend.espeak.words_mismatch import WordMismatch
from phonemizer.punctuation import Punctuation
from phonemizer.separator import Separator
from .base_tokenizer import BaseTokenizer

class EnglishTokenizer(BaseTokenizer):
    """Tokenizer for English text using Espeak."""

    def __init__(
        self,
        language="en-us",
        backend="espeak",
        separator=Separator(word="_", syllable="-", phone="|"),
        preserve_punctuation=True,
        punctuation_marks: Union[str, Pattern] = Punctuation.default_marks(),
        with_stress: bool = False,
        tie: Union[bool, str] = False,
        language_switch: LanguageSwitch = "keep-flags",
        words_mismatch: WordMismatch = "ignore",
    ) -> None:
        self.backend = EspeakBackend(
            language,
            punctuation_marks=punctuation_marks,
            preserve_punctuation=preserve_punctuation,
            with_stress=with_stress,
            tie=tie,
            language_switch=language_switch,
            words_mismatch=words_mismatch,
        )
        self.separator = separator

    def _to_list(self, phonemized: str) -> List[str]:
        """Convert phonemized string to list of phonemes."""
        fields = []
        for word in phonemized.split(self.separator.word):
            pp = re.findall(r"\w+|[^\w\s]", word, re.UNICODE)
            fields.extend(
                [p for p in pp if p != self.separator.phone]
                + [self.separator.word]
            )
        return fields[:-1]

    def phonemize(self, text: str, strip: bool = True) -> List[str]:
        """Convert English text to phonemes."""
        if not text.strip():
            return []
            
        # Handle single text input
        phonemized = self.backend.phonemize(
            [text], 
            separator=self.separator, 
            strip=strip, 
            njobs=1
        )
        
        # Convert to list of phonemes
        return self._to_list(phonemized[0])