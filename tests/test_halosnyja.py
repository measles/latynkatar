# Try to import from module, else import from the source code
try:
    import latynkatar
except ModuleNotFoundError:
    import src.latynkatar as latynkatar


def test_ju():
    assert latynkatar.convert("ЮрліВец лЮбіЦь лІю п'ю") == "JurliViec lUbiĆ lIju pju"


def test_ja():
    assert latynkatar.convert("Яз'яваЗЯпазЬяВА") == "JazjavaZIapaźjaVA"
