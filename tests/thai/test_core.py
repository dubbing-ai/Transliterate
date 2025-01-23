import pytest
from transliterate.thai.core import convert_text_to_ipa

class TestThaiCore:
    def test_basic_words(self):
        """Test basic Thai words conversion"""
        test_cases = [
            ("สวัสดี", "sa2.wat2.diː1"),
            ("ครับ", "kʰrap4"),
            ("มาก", "maːk3"),
            ("ขอบคุณ", "kʰᴐːp2.kʰun1"),
            ("ไทย", "tʰaj1"),
        ]
        for input_text, expected in test_cases:
            assert convert_text_to_ipa(input_text) == expected

    def test_compound_words(self):
        """Test compound Thai words"""
        test_cases = [
            ("น้ำตา", "naːm4.taː1"),
            ("ความรัก", "kʰwaːm1.rak4"),
            ("ความสุข", "kʰwaːm1.suk2"),
            ("บ้านเรือน", "baːn3.rɯːan1"),
            ("นกฮูก", "nok4.huːk3"),
        ]
        for input_text, expected in test_cases:
            assert convert_text_to_ipa(input_text) == expected
    
    def test_long_text_with_out_spaces(self):
        """Test long text without spaces"""
        test_cases = [
            ("สวัสดีครับผมชื่อนายแดงยินดีที่ได้รู้จัก", "sa2.wat2.diː1 kʰrap4 pʰom5 cʰɯː3 naːj1 dɛːŋ1 jin1.diː1 tʰiː3 daːj3 ruː4.cak2"),
            ("ฝนตกปรอยกรกนกคนตลกชวนดวงกมล", "fon5.tok2 prᴐːj1 kᴐːn1 ka2.nok2 kʰon1 ta2.lok2 cʰuːan1 duːaŋ1.ka2.mon1"),
            ("เรากินข้าวเช้ากับน้ำเต้าหู้", "raw1 kin1 kʰaːw3 cʰaw4 kap2 naːm4.taw3.huː3"),
        ]
        for input_text, expected in test_cases:
            assert convert_text_to_ipa(input_text) == expected

    def test_long_text_with_spaces(self):
        """Test long text with spaces"""
        test_cases = [
            ("ถ้าเราร่วมมือกัน ทำงานนี้ให้เสร็จ เราจะมีเวลาไปพักผ่อนมากขึ้น", "tʰaː3 raw1 ruːam3.mɯː1 kan1 tʰam1.ŋaːn1 niː4 haj3 set2 raw1 ca2 miː1 weː1.laː1 paj1 pʰak4.pʰᴐːn2 maːk3 kʰɯn3"),
            ("ชาวนาเดินออกจากบ้าน ระหว่างทางพบงูเห่า นอนตัวแข็งใกล้ตาย", "cʰaːw1.naː1 dɤːn1 ʔᴐːk2 caːk2 baːn3 ra4.waːŋ2.tʰaːŋ1 pʰop4 ŋuː1.haw2 nᴐːn1 tuːa1 kʰɛŋ5 klaj3.taːj1"),
            ("หลายวันต่อมา ขณะที่ราชสีห์ออกล่าเหยื่อ บังเอิญพลาดท่าไปติดกับดัก", "laːj5 wan1 tᴐː2.maː1 kʰa2.na2.tʰiː3 raːt3.cʰa4.siː5 ʔᴐːk2 laː3 jɯːa2 baŋ1.ʔɤːn1 pʰlaːt3.tʰaː3 paj1 tit2 kap2.dak2"),
        ]
        for input_text, expected in test_cases:
            assert convert_text_to_ipa(input_text) == expected

    def test_exception_words(self):
        """Test words with special pronunciation rules"""
        test_cases = [
            ("เฮี๊ยะ", "hia4"),
            ("เซี๊ย", "siːa4"),
            ("แทรก", "sɛːk3"),
            ("พุทรา", "pʰut4.saː1"),
            ("ทริป", "tʰrip4"),
            ("ฉะเชิงเทรา", "cʰa2.cʰɤːŋ1.saw1")
            ("โหงวเฮ้ง", "ŋoː5.heːŋ4"),
            ("ลานจอดฮ", "laːn1.cᴐːt2 hᴐː1"),
            ("หมง", "moŋ5"),
            ("โหมงาน", "hoːm5 ŋaːn1"),
            ("คฤหาสน์", "kʰa4.rɯ4.haːt2"),
            ("พฤหัสบดี", "pʰa4.rɯ4.hat2.sa2.bᴐː1.diː1"),
            ("ทฤษฎี", "tʰrit4.sa2.diː1"),
        ]
        for input_text, expected in test_cases:
            assert convert_text_to_ipa(input_text) == expected

    def test_sentence_with_exceptions_word(self):
        """Test sentence with exception words"""
        test_cases = [
            ("ต้นไทรต้นนี้สวยจังรากมันชอนไชไปทุกที่", "ton3.saj1 ton3 niː4 suːaj5 caŋ1 raːk3 man1 cʰᴐːn1.cʰaj1 paj1 tʰuk4 tʰiː3"),
            ("เราต้องเข้าแทรกแซง", "raw1 tᴐːŋ3 kʰaw3.sɛːk3.sɛːŋ1"),
            ("ทริปเขาใหญ่", "tʰrip4 kʰaw5 jaj2"),
            ("อย่าปล่อยให้มันทรุดโทรม", "jaː2 plᴐːj2 haj3 man1 sut4.soːm1"),
        ]
        for input_text, expected in test_cases:
            assert convert_text_to_ipa(input_text) == expected

    def test_foreign_words(self):
        """Test transliterated foreign words"""
        test_cases = [
            ("เจฟฟรี่", "ceːp4.friː3"),
            ("โฮล์ม", "hoːm1"),
            ("ดรากอน", "draː1.kᴐːn1"),
        ]
        for input_text, expected in test_cases:
            assert convert_text_to_ipa(input_text) == expected

    def test_sentence_with_foreign_words(self):
        """Test sentence with foreign words"""
        test_cases = [
            ("เจฟฟรี่เป็นคนดี", "ceːp4.friː3 pen1 kʰon1 diː1"),
            ("สวัสดีครับคุณโฮล์ม", "sa2.wat2.diː1 kʰrap4 kʰun1 hoːm1"),
            ("นั่นดรากอนนอนอยู่", "nan3 draː1.kᴐːn1 nᴐːn1 juː2"),
        ]
        for input_text, expected in test_cases:
            assert convert_text_to_ipa(input_text) == expected

    def test_whitespace_handling(self):
        """Test handling of whitespace"""
        test_cases = [
            ("  สวัสดี  ", "sa2.wat2.diː1"),
            ("สวัสดี ครับ", "sa2.wat2.diː1 kʰrap4"),
            ("สวัสดี  ครับ", "sa2.wat2.diː1 kʰrap4"),
            ("\nสวัสดี\t", "sa2.wat2.diː1"),
        ]
        for input_text, expected in test_cases:
            assert convert_text_to_ipa(input_text) == expected

    def test_edge_cases(self):
        """Test edge cases and error handling"""
        assert convert_text_to_ipa("") == ""
        assert convert_text_to_ipa(" ") == ""
        assert convert_text_to_ipa("\n\t ") == ""

    def test_punctuation_handling(self):
        """Test handling of text with punctuation"""
        test_cases = [
            ("สวัสดี!", "sa2.wat2.diː1"),
            ("สวัสดี, ครับ", "sa2.wat2.diː1 kʰrap4"),
            ("สวัสดี...", "sa2.wat2.diː1"),
            ("(สวัสดี)", "sa2.wat2.diː1"),
        ]
        for input_text, expected in test_cases:
            assert convert_text_to_ipa(input_text) == expected