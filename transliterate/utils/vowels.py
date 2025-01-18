class Vowels:
    """Class containing Thai vowel configurations and utilities."""
    
    def __init__(self):
        self.short_monophthongs = [
            'a', 'e', 'ɛ', 'i', 'o', 'ᴐ', 'u', 'ɯ', 'ɤ'
        ]
        self.long_monophthongs = [
            'aː', 'eː', 'ɛː', 'iː', 'oː', 'ᴐː', 'uː', 'ɯː', 'ɤː'
        ]
        self.diphthongs = [
            'ia', 'ua', 'ɯa'
        ]
        # Ensure that longer vowels are checked first
        self.all_vowels = self.diphthongs + self.long_monophthongs + self.short_monophthongs
        self.all_vowels.sort(key=len, reverse=True)