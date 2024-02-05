import pytest
from src.latynkatar import Cyr2Lat

# Узор узяты з часопіса PAMYŁKA: 
# https://github.com/PAMYLKA-ZIN/pamylka-number-3/tree/main/PAMYLKA_ZIN_3_FOR_SHARING
PRYKŁAD = """Вітаем цябе, чытачу!
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
UZOR = """Vitajem ciabie, čytaču!
Heta treci numar PAMYŁKA ZIN!
My vielmi ciešymsia, što da kamandy stvaralnikaǔ praciahvajuć dałučacca
novyja navukoǔcy i mastaki! J my budziem radyja kožnamu novamu ǔdzielniku!
Siabry, my redakcyjaj nadumali zapačatkavać premiju – «Bizon Higs». Tamu hety
numar my prysviačajem usim biełaruskim navukoǔcam i chočam anansavać premiju,
jakaja budzie ǔvasablać saboj Biełaruś i navuku razam! Heta ǔznaharoda dla
biełaruskich navukoǔcaǔ i daslednikaǔ dakładnych i pryrodaznaǔčych navuk ad
navukova-papularnaha časopisu Pamyłka Zin.
Bolš detalaǔ apaviadaje pieršy artykuł numaru.
"""

def test_pryład():
    assert Cyr2Lat.convert(PRYKŁAD) == UZOR