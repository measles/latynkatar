# Try to import from module, else import from the source code
try:
    from latynkatar import Cyr2Lat
except ModuleNotFoundError:
    from src.latynkatar import Cyr2Lat


def test_l():
    assert Cyr2Lat.convert("ЛаЭлЯЛуЛіЛюЛЁлЕлЬ лЛя") == "ŁaElAŁuLiLuLOlEl lLa"
    
def test_ch():
    assert Cyr2Lat.convert("ХаХу ХЫВАХххххх Хіх") == "ChaChu ChYVAChchchchchch Chich"
