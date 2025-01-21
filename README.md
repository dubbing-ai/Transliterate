# Transliterate

A Python library for converting text into IPA (International Phonetic Alphabet) and phoneme representations, supporting both English and Thai languages. This library is designed for linguistic processing, speech synthesis, and phonetic analysis of text.

## Features

- English text to phoneme conversion using eSpeak
- Thai text to IPA and phoneme conversion
  - Custom word tokenization
  - Special pronunciation cases
  - Comprehensive vowel system including monophthongs and diphthongs
- Modular tokenizer architecture with extensible base classes
- Support for custom pronunciation exceptions
- Comprehensive vowel handling for Thai language

## Prerequisites

- Python 3.8 or higher
- eSpeak library (for English phoneme conversion)
- PyThaiNLP (for Thai language processing)
- TLTK (for Thai language processing)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/dubbing-ai/Transliterate.git
cd Transliterate
```

2. Install the package using Poetry:

```bash
poetry install
```

## Usage

### English Text to Phonemes

```python
from transliterate.phonemizer import EnglishPhonemizer, setup_espeak

# Initialize the phonemizer
english_phonemizer = EnglishPhonemizer()

# Convert English text to phonemes
text = "hippopotamus"
phonemes = english_phonemizer.phonemize(text)
print(f"English phonemes: {phonemes}")
# Output: ['h', 'ɪ', 'p', 'ə', 'p', 'ɑː', 'ɾ', 'æ', 'm', 'ə', 's']
```

### Thai Text to Phonemes

```python
from transliterate.phonemizer import ThaiPhonemizer

# Initialize the phonemizer
thai_phonemizer = ThaiPhonemizer()

# Convert Thai text to phonemes
text = "สวัสดี"
phonemes = thai_phonemizer.phonemize(text)
print(f"Thai phonemes: {phonemes}")
# Output: ['s', 'a2', 'w', 'a2', 't', 'd', 'iː']
```

### Setup espeak (optional)

```python
from transliterate.tokenizer import setup_espeak
setup_espeak('/path/to/libespeak.dylib')
```

## Project Structure

```plaintext
transliterate/
├── phonemizer/
│   ├── __init__.py
│   ├── base_phonemizer.py     # Abstract base class for phonemizers
│   ├── english_phonemizer.py  # English language phonemizer
│   ├── thai_phonemizer.py     # Thai language phonemizer
│   └── utils.py               # Utility functions
├── thai/
│   ├── core.py               # Thai text to IPA conversion
│   ├── exceptions.py         # Special case handling for Thai words or syllables
│   └── tokenizer.py          # Custom word tokenization
└── utils/
    ├── phoneme_converter.py  # IPA to phoneme conversion
    ├── punctuations.py       # Punctuation handling
    └── vowels.py             # Thai vowel configurations
```

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

## Acknowledgments

- [PyThaiNLP](https://github.com/PyThaiNLP/pythainlp) for providing Thai NLP tools.
- [TLTK](https://github.com/tlkunited/tltk) for Thai linguistic processing.
- [eSpeak](https://github.com/espeak-ng/espeak-ng) - for English phoneme conversion

## Contact

For questions or support, feel free to reach out at [thanat.wongsamut@gmail.com].
