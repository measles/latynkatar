import pytest
from src.latynkatar import Cyr2Lat


def test_l():
    assert Cyr2Lat.convert("ЛаЭлЯЛуЛіЛюЛЁлЕлЬ") == "ŁaElAŁuLiLuLOlEl"
