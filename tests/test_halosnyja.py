# Try to import from module, else import from the source code
try:
    from latynkatar import Cyr2Lat
except ModuleNotFoundError:
    from src.latynkatar import Cyr2Lat


def test_ju():
    assert Cyr2Lat.convert("ЮрліВец лЮбіЦь лІю п'ю") == "JurliViec lUbiĆ lIju pju"
