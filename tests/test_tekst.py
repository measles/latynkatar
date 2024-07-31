# Try to import from module, else import from the source code
try:
    from latynkatar import Cyr2Lat
except ModuleNotFoundError:
    from src.latynkatar import Cyr2Lat

from time import monotonic

# Узор узяты з часопіса PAMYŁKA:
# https://github.com/PAMYLKA-ZIN/pamylka-number-3/tree/main/PAMYLKA_ZIN_3_FOR_SHARING
PRYKŁAD_PAMYŁKA = """Вітаем цябе, чытачу!
Гэта трэці нумар PAMYŁKA ZIN!
Мы вельмі цешымся, што да каманды стваральнікаў працягваюць далучацца
новыя навукоўцы і мастакі! І мы будзем радыя кожнаму новаму ўдзельніку!
Сябры, мы рэдакцыяй надумалі запачаткаваць прэмію – «Бізон Гіґс». Таму гэты
нумар мы прысвячаем усім беларускім навукоўцам і хочам анансаваць прэмію,
якая будзе ўвасабляць сабой Беларусь і навуку разам! Гэта ўзнагарода для
беларускіх навукоўцаў і даследнікаў дакладных і прыродазнаўчых навук ад
навукова-папулярнага часопісу Pamyłka Zin.
Больш дэталяў апавядае першы артыкул нумару.
"""
UZOR_PAMYŁKA = """Vitajem ciabie, čytaču!
Heta treci numar PAMYŁKA ZIN!
My vielmi ciešymsia, što da kamandy stvaralnikaŭ praciahvajuć dałučacca
novyja navukoŭcy i mastaki! I my budziem radyja kožnamu novamu ŭdzielniku!
Siabry, my redakcyjaj nadumali zapačatkavać premiju – «Bizon Higs». Tamu hety
numar my pryśviačajem usim biełaruskim navukoŭcam i chočam anansavać premiju,
jakaja budzie ŭvasablać saboj Biełaruś i navuku razam! Heta ŭznaharoda dla
biełaruskich navukoŭcaŭ i daślednikaŭ dakładnych i pryrodaznaŭčych navuk ad
navukova-papularnaha časopisu Pamyłka Zin.
Bolš detalaŭ apaviadaje pieršy artykuł numaru.
"""
UZOR_PAMYŁKA_KLASIČNY = """Witajem ciabie, czytaczu!
Heta treci numar PAMYŁKA ZIN!
My wielmi cieszymsia, szto da kamandy stwaralnikaŭ praciahwajuć dałuczacca
nowyja nawukoŭcy i mastaki! I my budziem radyja kożnamu nowamu ŭdzielniku!
Siabry, my redakcyjaj nadumali zapaczatkawać premiju – «Bizon Higs». Tamu hety
numar my pryświaczajem usim biełaruskim nawukoŭcam i choczam anansawać premiju,
jakaja budzie ŭwasablać saboj Biełaruś i nawuku razam! Heta ŭznaharoda dla
biełaruskich nawukoŭcaŭ i daślednikaŭ dakładnych i pryrodaznaŭczych nawuk ad
nawukowa-papularnaha czasopisu Pamyłka Zin.
Bolsz detalaŭ apawiadaje pierszy artykuł numaru.
"""

PRYKŁAD_BAHDANOVIČ = """Маладыя гады,
Маладыя жаданні!
Ні жуды, ні нуды,
Толькі шчасьце каханьня!
 
Помніш толькі красу,
Мілы тварык дзявочы,
Залатую касу,
Сіняватыя вочы!

Цёмны сад-вінаград,
Цьвет бяленькі вішнёвы, —
І агністы пагляд,
І гарачыя словы!
 
Будзь жа, век малады,
Поўны сьветлымі днямі!
Пралятайце, гады,
Залатымі агнямі!
"""
UZOR_BAHDANOVIČ = """Maładyja hady,
Maładyja žadańni!
Ni žudy, ni nudy,
Tolki ščaście kachańnia!
 
Pomniš tolki krasu,
Miły tvaryk dziavočy,
Załatuju kasu,
Siniavatyja vočy!

Ciomny sad-vinahrad,
Ćviet bialeńki višniovy, —
I ahnisty pahlad,
I haračyja słovy!
 
Budź ža, viek małady,
Poŭny śvietłymi dniami!
Pralatajcie, hady,
Załatymi ahniami!
"""
UZOR_BAHDANOVIČ_KLASICZNY = """Maładyja hady,
Maładyja żadańni!
Ni żudy, ni nudy,
Tolki szczaście kachańnia!
 
Pomnisz tolki krasu,
Miły twaryk dziawoczy,
Załatuju kasu,
Siniawatyja woczy!

Ciomny sad-winahrad,
Ćwiet bialeńki wiszniowy, —
I ahnisty pahlad,
I haraczyja słowy!
 
Budź ża, wiek małady,
Poŭny świetłymi dniami!
Pralatajcie, hady,
Załatymi ahniami!
"""

with open("tests/data/novaja_ziamla.txt", "r") as novy_fail:
    NOVAJA_ZIAMLA = novy_fail.read()


def test_z_pamylki():
    assert Cyr2Lat.convert(PRYKŁAD_PAMYŁKA) == UZOR_PAMYŁKA


def test_z_pamylki_klasiczny():
    assert Cyr2Lat.convert_classic(PRYKŁAD_PAMYŁKA) == UZOR_PAMYŁKA_KLASIČNY


def test_bahdanovicz():
    assert Cyr2Lat.convert(PRYKŁAD_BAHDANOVIČ) == UZOR_BAHDANOVIČ


def test_bahdanovicz_klasiczny():
    assert Cyr2Lat.convert_classic(PRYKŁAD_BAHDANOVIČ) == UZOR_BAHDANOVIČ_KLASICZNY


def test_novaj_ziamloju():
    start = monotonic()
    _ = Cyr2Lat.convert(NOVAJA_ZIAMLA)
    finish = monotonic()

    time_required = finish - start

    print(start, finish, time_required)

    assert time_required < 0.5


def test_novaj_ziamloju_klasicny():
    start = monotonic()
    _ = Cyr2Lat.convert_classic(NOVAJA_ZIAMLA)
    finish = monotonic()

    time_required = finish - start

    print(start, finish, time_required)

    assert time_required < 0.5
