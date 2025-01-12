from transliterate.tokenizer import EnglishTokenizer, ThaiTokenizer, setup_espeak

def main():
    # Set up espeak library
    _ESPEAK_LIBRARY = '/opt/homebrew/Cellar/espeak/1.48.04_1/lib/libespeak.1.1.48.dylib'
    setup_espeak(_ESPEAK_LIBRARY)
    
    # Initialize tokenizers
    english_tokenizer = EnglishTokenizer()
    thai_tokenizer = ThaiTokenizer()
    
    # Test English tokenization
    english_text = "hippopotamus"
    ph_en = english_tokenizer.phonemize(english_text)
    print(f"English phonemes: {ph_en}")
    
    # Test Thai tokenization
    thai_text = "สวัสดี"
    ph_th = thai_tokenizer.phonemize(thai_text)
    print(f"Thai phonemes: {ph_th}")

if __name__ == "__main__":
    main()