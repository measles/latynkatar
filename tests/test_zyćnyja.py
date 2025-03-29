# Try to import from module, else import from the source code
try:
    import latynkatar
except ModuleNotFoundError:
    import src.latynkatar as latynkatar


def test_l():
    assert latynkatar.convert("ЛаЭлЯЛуЛіЛюЛЁлЕлЬ лЛя") == "ŁaElAŁuLiLuLOlEl lLa"


def test_ch():
    assert latynkatar.convert("ХаХу ХЫВАХххххх Хіх") == "ChaChu ChYVAChchchchchch Chich"


def test_sz():
    assert latynkatar.convert_old("ШашуШышшшшшшш") == "SzaszuSzyszszszszszszsz"


def test_š():
    assert latynkatar.convert("ШашуШышшшшшшш") == "ŠašuŠyššššššš"


def test_cz():
    assert latynkatar.convert_old("чАЧыЧУ") == "czACzyCzU"


def test_č():
    assert latynkatar.convert("чАЧыЧУ") == "čAČyČU"


def test_ż():
    assert latynkatar.convert_old("жУрАвІнЫЖэЖЫ") == "żUrAwInYŻeŻY"


def test_ž():
    assert latynkatar.convert("жУрАвІнЫЖэЖЫ") == "žUrAvInYŽeŽY"


def test_w():
    assert latynkatar.convert_old("войт і Ваявода") == "wojt i Wajawoda"


def test_v():
    assert latynkatar.convert("войт і Ваявода") == "vojt i Vajavoda"


def test_miakkaści():
    assert (
        latynkatar.convert("снег смех поспех святы Валянцін жаданні пустазелле")
        == "śnieh śmiech pośpiech śviaty Valancin žadańni pustazielle"
    )


def test_biez_miakkaści():
    assert (
        latynkatar.convert(
            "снег смех поспех святы Валянцін жаданні пустазелле", miakkasc=False
        )
        == "snieh smiech pospiech sviaty Valancin žadanni pustazielle"
    )
