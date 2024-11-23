# Try to import from module, else import from the source code
try:
    from latynkatar import Cyr2Lat
except ModuleNotFoundError:
    from src.latynkatar import Cyr2Lat


def test_l():
    assert Cyr2Lat.convert("ЛаЭлЯЛуЛіЛюЛЁлЕлЬ лЛя") == "ŁaElAŁuLiLuLOlEl lLa"


def test_ch():
    assert Cyr2Lat.convert("ХаХу ХЫВАХххххх Хіх") == "ChaChu ChYVAChchchchchch Chich"


def test_sz():
    assert Cyr2Lat.convert_classic("ШашуШышшшшшшш") == "SzaszuSzyszszszszszszsz"


def test_š():
    assert Cyr2Lat.convert("ШашуШышшшшшшш") == "ŠašuŠyššššššš"


def test_cz():
    assert Cyr2Lat.convert_classic("чАЧыЧУ") == "czACzyCzU"


def test_č():
    assert Cyr2Lat.convert("чАЧыЧУ") == "čAČyČU"


def test_ż():
    assert Cyr2Lat.convert_classic("жУрАвІнЫЖэЖЫ") == "żUrAwInYŻeŻY"


def test_ž():
    assert Cyr2Lat.convert("жУрАвІнЫЖэЖЫ") == "žUrAvInYŽeŽY"


def test_w():
    assert Cyr2Lat.convert_classic("войт і Ваявода") == "wojt i Wajawoda"


def test_v():
    assert Cyr2Lat.convert("войт і Ваявода") == "vojt i Vajavoda"


def test_miakkaści():
    assert (
        Cyr2Lat.convert("снег смех поспех святы Валянцін жаданні")
        == "śnieh śmiech pośpiech śviaty Valancin žadańni"
    )
