from abc import ABC, abstractmethod
from typing import List, Optional

class BasePhonemizer(ABC):
    """Base class for text phonemizer."""
    
    @abstractmethod
    def phonemize(self, text: str, strip: bool = True) -> List[str]:
        """Convert text to phonemes.
        
        Args:
            text (str): Input text
            strip (bool): Whether to strip whitespace
            
        Returns:
            List[str]: List of phonemes
        """
        pass
