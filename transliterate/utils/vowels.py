class Vowels:
    """Class containing Thai vowel configurations and utilities."""
    
    def __init__(self):
        self.short_monophthongs = [
            'a', 'e', 'ɛ', 'i', 'o', 'ᴐ', 'u', 'ɯ', 'ɤ'
        ]
        self.long_monophthongs = [
            'aː', 'eː', 'ɛː', 'iː', 'oː', 'ᴐː', 'uː', 'ɯː', 'ɤː'
        ]
        self.short_diphthongs = [
            'ia', 'ua', 'ɯa'
        ]
        self.long_diphthongs = [
            'iːa', 'uːa', 'ɯːa'
        ]
        # Ensure that longer vowels are checked first
        self.all_vowels = self.long_diphthongs + self.short_diphthongs + self.long_monophthongs + self.short_monophthongs
        self.all_vowels.sort(key=len, reverse=True)