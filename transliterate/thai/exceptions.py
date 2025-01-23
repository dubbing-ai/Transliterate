def exceptionWords(word: str) -> str:
    """
    Handle exception cases for Thai words that need special transliteration.
    
    Args:
        word (str): Input Thai word
        
    Returns:
        str: Special IPA representation for exception words
    """
    dictionary = {
        'เฮี๊ยะ': 'hia4', # ia เอียสั้น
        'เซี๊ย': 'siːa4', # i:a เอียยาว
        'เชี๊ย': 'cʰiːa4',
        'เริ่ด': 'rɤt3', # เริด = rɤːt3 -> เริ่ด = rɤt3
        'กษัตริย์': 'ka2.sat2',
        'ครํ่า': 'kʰram3',
        'หวอด': 'wᴐːt2',
        'ครํ่าหวอด': 'kʰram3.wᴐːt2',
        'เนี่ยะ': 'nia3',
        'สจ๊วร์ต': 'sa2.cuːat4', # referred from 'สจ๊วด'
        'ฮ': 'hᴐː1',
        'หมง': 'moŋ5',
        # ทร-
        'แทรก': 'sɛːk3',
        'แทรง': 'sɛːŋ1',
        'โทรม': 'soːm1',
        'ไทร': 'saj1',
        'ทริป': 'tʰrip4',
        'ฉะเชิงเทรา': 'cʰa2.cʰɤːŋ1.saw1',
        # Transliteration
        'เจฟ': 'ceːp4',
        'ฟรี่': 'friː3',
        'โฮล์ม': 'hoːm1',
        'ดรากอน': 'draː1.kᴐːn1',
        'เคลา': 'kʰlaw1',
        'โจช': 'coːt1',
        'โวล์ฟ': 'woːp3',
        'โหงวเฮ้ง': 'ŋoː5.heːŋ4',
        # RU
        'อฤศราณ์': 'ʔa2 rit4 sa2 raː1',
    }
    return dictionary.get(word, '')
