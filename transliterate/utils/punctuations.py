class Punctuations:
    """Class containing punctuations"""
    
    def __init__(self):
        self.all_punctuations = [
            '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
        ]

    def remove_punctuations(self, text: str) -> str:
        """Remove all punctuations from text."""
        return ''.join([char if char not in self.all_punctuations else ' ' for char in text])
