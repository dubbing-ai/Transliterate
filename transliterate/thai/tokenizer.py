from pythainlp.tokenize import Tokenizer
from pythainlp.corpus.core import get_corpus
from pythainlp.util import dict_trie


def CustomTokenizer() -> Tokenizer:
    """
    Creates a custom tokenizer with additional Thai words for special word tokenization.
    
    The tokenizer combines the core Thai dictionary with custom words specific to the
    project's needs, using a trie-based dictionary structure for efficient tokenization.
    
    Returns:
        Tokenizer: A custom tokenizer instance with enhanced word recognition.
    """
    # Get the core Thai dictionary
    thai_words = get_corpus('words_th.txt')

    # Define custom words for specific tokenization needs
    custom_words = {
        'เจฟฟรี่',
        'ไฟน์สโตน',
        'ไฮด์',
        'โกล์ด',
        'โฮล์ม'
    }

    # Combine core dictionary with custom words
    all_words = list(custom_words) + list(thai_words)

    # Create trie dictionary for efficient lookup
    custom_dict_trie = dict_trie(dict_source=all_words)

    # Initialize tokenizer with custom dictionary
    return Tokenizer(custom_dict=custom_dict_trie, engine='newmm')