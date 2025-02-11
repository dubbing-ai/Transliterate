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
        'พระมหากษัตริย์': 'pʰra2.ma4.haː5.ka2.sat2',
        'มหากษัตริย์': 'ma4.haː5.ka2.sat2',
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

        # RU
        'อฤศราณ์': 'ʔa2 rit4 sa2 raː1',

        # Hard Thai words
        'เส้นผ่านศูนย์กลาง': 'seːn3.pʰaːn2.suːn5.klaːŋ1',
        'โทรศัพท์': 'tʰoː1.ra4.sap2',
        'ครุฑพ่าห์': 'kʰrut4.pʰaː3',
        'เครื่องหมายครุฑพ่าห์': 'kʰrɯːaŋ3.maːj5 kʰrut4.pʰaː3',
        'โบสถ์': 'boːt2',
        'อัญญา': 'ʔan1.ja1',
        'โกณฑัญญะ': 'koːn1.tʰan1.ja4',
        'วัดมกุฏกษัตริย์': 'wat4.ma4.kut2.ka2.sat2',
        'กริยาคุณศัพท์': 'kri2.jaː1.kʰun1.na4.sap2',
        'ทรัพย์สินส่วนพระมหากษัตริย์': 'sap4.sin5.suːan2.pʰra4.ma4.haː5.ka2.sat2',
        'พลา': 'pʰlaː1',
        'พลานุภาพ': 'pʰa4.laː1.nu4.pʰaːp3',
        'พลานามัย': 'pʰa4.laː1.naː1.maj1',
        
        # Transliteration
        'เจฟ': 'ceːp4',
        'ฟรี่': 'friː3',
        'โฮล์ม': 'hoːm1',
        'ดรากอน': 'draː1.kᴐːn1',
        'ดราก้อน': 'draː1.kᴐːn3',
        'เคลา': 'kʰlaw1',
        'โจช': 'coːt1',
        'โวล์ฟ': 'woːp3',
        'โหงวเฮ้ง': 'ŋoː5.heːŋ4',
        'ลอร์ด': 'lɔːt2',
        'แมชชีน': 'mɛːt3.cʰiːn1',
        'ฟาเรนไฮต์': 'faː1.reːn1.haj1',
        'วินโดวส์': 'win1.doːw1',
        'เกรกอรี': 'kreː1.kᴐː1.riː1',
        'เบตสัน': 'bet4.san5',
        'แรคคูน': 'rɛːk3.kʰuːn1',
        'อินดัสตรีส์': 'ʔin1.dat4.triː3',
        'นอร์ทแคโรไลนา': 'nᴐːt3.kʰɛː1.roː1.laj1.naː1',
        'โพรดัคท์': 'pʰroːdak2',
        'อินเตอร์เน็ต': 'ʔin1.tɤː1.net2',
        'พอดแคสต์': 'pʰᴐːt2.kʰɛːt4',
        'ยูทูป': 'juː1.tʰuːp4',
        'รีโมต': 'riː1.moːt2',
        'รีโมท': 'riː1.moːt2',
        'เฟซบุ๊ก': 'feːt4.buk4',
        'ซอฟต์': 'sᴐːp4',
        'แอส': 'ʔɛːt4',
        'โตร': 'troː1',
        'เทิร์ฟ': 'tʰɤːp4',
        'เคนนี': 'kʰeːn1.niː3',
        'เกอร์': 'kɤː3',
        'เซคชัน': 'sek4.cʰan3',
        'มิสเตอร์': 'mit4.tɤː1',

        # Transliteration (with "l" ending)
        'คูล': 'kʰuːw1',
        'เคลวิน': 'kʰeːw1.win3',
        'รีเทล': 'riː1.tʰeːw1',
        'เบงกอล': 'beːŋ1.kᴐːw1',
        'เวิลด์': 'wɤːw1',
        'ทรัล': 'tʰraw3',
        'เซ็นทรัล': 'sen1.tʰraw3',
        'เซ็นทรัลเวิร์ล': 'sen1.tʰraw3.wɤːw1',
        'เซ็นทรัลเวิลด์': 'sen1.tʰraw3.wɤːw1',
        'เซ็นทรัลพลาซา': 'sen1.tʰraw3.pʰlaː1.saː1',
        'เซ็นทรัลอินเตอร์พัฒนา': 'sen1.tʰraw3.ʔin1.tɤː3.pʰat4.tʰa4.naː1',
        'คอล': 'kʰᴐːw1',
        'คอลส์': 'kʰᴐːw3',
        'โปรโตคอล': 'proː1.toː1.kʰᴐːw1',
        'เม็ททัล': 'met4.tʰaw3',
        'ออลล์': 'ʔᴐːw1',
        'เวล': 'weːw1',
        'เดล': 'deːw1'
    }
    return dictionary.get(word, '')
