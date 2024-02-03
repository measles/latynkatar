import pytest
from latynkatar import Cyr2Lat


def test_l():
    assert Cyr2Lat.convert("ЛаЭлЯЛуЛіЛюЛЁлЕлЬ") == "ŁaElAŁuLiLuLOlEl"


def test_ju():
    assert Cyr2Lat.convert("ЮрліВец лЮбіЦь лІю п'ю") == "JurliViec lUbiĆ lIju pju"
