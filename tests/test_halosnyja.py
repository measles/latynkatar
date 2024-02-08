import pytest
from src.latynkatar import Cyr2Lat


def test_ju():
    assert Cyr2Lat.convert("ЮрліВец лЮбіЦь лІю п'ю") == "JurliViec lUbiĆ lIju pju"
