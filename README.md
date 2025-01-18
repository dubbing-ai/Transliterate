# Transliterate

A Python library for converting text into IPA (International Phonetic Alphabet) and phoneme representations, supporting both English and Thai languages. This library is designed for linguistic processing, speech synthesis, and phonetic analysis of text.

## Features

- English text to phoneme conversion using eSpeak
- Thai text to IPA and phoneme conversion
- Modular tokenizer architecture with extensible base classes
- Support for custom pronunciation exceptions
- Comprehensive vowel handling for Thai language

## Prerequisites

- Python 3.8 or higher
- eSpeak library (for English phoneme conversion)
- PyThaiNLP
- TLTK

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
from transliterate.tokenizer import EnglishTokenizer

# Initialize the tokenizer
english_tokenizer = EnglishTokenizer()

# Convert English text to phonemes
text = "hippopotamus"
phonemes = english_tokenizer.phonemize(text)
print(f"English phonemes: {phonemes}")
```

### Thai Text to Phonemes

```python
from transliterate.tokenizer import ThaiTokenizer

# Initialize the tokenizer
thai_tokenizer = ThaiTokenizer()

# Convert Thai text to phonemes
text = "สวัสดี"
phonemes = thai_tokenizer.phonemize(text)
print(f"Thai phonemes: {phonemes}")
```

### Setup espeak (optional)

```python
from transliterate.tokenizer import setup_espeak
setup_espeak('/path/to/libespeak.dylib')
```

## Project Structure

```plaintext
transliterate/
├── thai/
│   ├── core.py               # Thai text to IPA conversion
│   └── exceptions.py         # Special case handling for Thai words
├── tokenizer/
│   ├── __init__.py
│   ├── base_tokenizer.py     # Abstract base class for tokenizers
│   ├── english_tokenizer.py  # English language tokenizer
│   ├── thai_tokenizer.py     # Thai language tokenizer
│   └── utils.py              # Utility functions
└── utils/
    ├── phoneme_converter.py  # IPA to phoneme conversion
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
