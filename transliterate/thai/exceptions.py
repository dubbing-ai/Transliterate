def exceptionWords(word: str) -> str:
    """
    Handle exception cases for Thai words that need special transliteration.
    
    Args:
        word (str): Input Thai word
        
    Returns:
        str: Special IPA representation for exception words
    """
    dictionary = {
        'เฮี๊ยะ': 'hia4',
        'เซี๊ย': 'si:a4',
        'เชี๊ย': 'cʰiːa4',
        'เริ่ด': 'rɤt3',
        'กษัตริย์': 'ka2.sat2',
        'ครํ่าหวอด': 'kʰram3.wᴐːt2',
        'เนี่ยะ': 'nia3',
        'สจ๊วร์ต': 'sa2.cuːat4',
    }
    return dictionary.get(word, '')