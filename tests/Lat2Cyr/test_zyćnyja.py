# Try to import from module, else import from the source code
try:
    from latynkatar import Lat2Cyr
except ModuleNotFoundError:
    from src.latynkatar import Lat2Cyr


def test_l():
    assert Lat2Cyr.convert("ŁaElAŁuLiLuLOlEl lLa") == "ЛаЭлЯЛуЛіЛюЛЁлЕлЬ лЛя"


def test_ch():
    assert Lat2Cyr.convert("ChaChu ChYVAChchchchchch Chich") == "ХаХу ХЫВАХххххх Хіх"


def test_š():
    assert Lat2Cyr.convert("ŠašuŠyššššššš") == "ШашуШышшшшшшш"


def test_č():
    assert Lat2Cyr.convert("čAČyČU") == "чАЧыЧУ"


def test_ž():
    assert Lat2Cyr.convert("žUrAvInYŽeŽY") == "жУрАвІнЫЖэЖЫ"


def test_v():
    assert Lat2Cyr.convert("vojt i Vajavoda") == "войт і Ваявода"
