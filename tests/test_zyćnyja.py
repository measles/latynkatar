import pytest
from latynkatar import Cyr2Lat


def test_l():
    assert Cyr2Lat.convert("ЛаЭлЯЛуЛіЛюЛЁлЕлЬ") == "ŁaElAŁuLiLuLOlEl"
