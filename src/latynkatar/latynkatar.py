"""
This file is part of Łatynkatar.

Łatynkatar is free software: you can redistribute it and/or modify it under the
terms of the GNU Lesser General Public License v3 (LGPLv3) as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

Łatynkatar is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Lesser General Public License v3 (LGPLv3) for
more details. In file LICENSE which should came with a package, or look at it
in the repo, see <https://github.com/measles/latynkatar/blob/main/LICENSE>.

You should have received a copy of the GNU Lesser General Public License v3
(LGPLv3) along with Łatynkatar. If not, see <https://www.gnu.org/licenses/>.

:copyright: (c) (c) 2025 Łatynkatar group: https://github.com/latynkatar
"""

from .variables import (
    HALOSNYJA,
    JOTAWANYJA_LITARY,
    KLASICZNYJA_PRAWILY_KANVERTACYJI,
    MOHUC_PAZNACZACCA_JAK_MIAKKIJA,
    PRAVILY_KANVERTACYJ,
    ZYCZNYJA_Z_TRANZITAM,
)


def _ci_patrabuje_adlustravannia_tranzityunaj_miakkasci(
    next_letter: str, next_next_letter: str
) -> bool:
    """Правярае, ці патрабуе пазіцыя зычнай адлюстравання транзітыўнай мяккасці.

    Args:
        next_letter (str): наступная літара
        next_next_letter (str): літара праз адну ад бягучай

    Returns:
        bool: True, калі патрабуе
    """
    return next_letter.lower() in ZYCZNYJA_Z_TRANZITAM and (
        next_next_letter.lower() in JOTAWANYJA_LITARY or next_next_letter.lower() == "ь"
    )


def _ci_patrabuje_j(previous_letter: str) -> bool:
    """Спраўджае, ці патрэбная пры канвертацыі ётаваных j.

    Args:
        previous_letter (str): папярэдняя літара ці сімвал

    Returns:
        bool: True, калі патрабуе
    """
    return (
        not previous_letter
        or previous_letter.lower() in HALOSNYJA
        or not previous_letter.isalpha()
        or previous_letter == "'"
        or previous_letter.lower() == "ь"
    )


def _kanvertavac_z_j(current_letter: str, previous_letter: str) -> str:
    """Канвертуе ў лацінку літары з j/i: і, е, ё, ю, я.

    Args:
        current_letter (str): Літара, каторую трэба сканвертаваць
        previous_letter (str): Пяпярэдняя літара ў тэксце, ці пусты радок,
            калі папярэдняе няма.

    Returns:
        str: Сканвертаваную да лацінкі літару. Вынікам часцяком можа быць
            некалькі літар.
    """
    if _ci_patrabuje_j(previous_letter) and current_letter.lower() != "і":
        base = "j"
    else:
        base = "i"

    second_letter = JOTAWANYJA_LITARY[current_letter.lower()]
    if (
        current_letter.lower() != "і"
        and previous_letter
        and previous_letter.lower() == "л"
    ):
        base = ""

    converted_letter = base + second_letter

    return converted_letter


def _miakkuja_zycznyja(
    current_letter: str,
    next_letter: str,
    next_next_letter: str,
    miakkasc: bool,
) -> str:
    """Канвертуе да лацінкі зычныя, якія могуць быць мяккімі.

    Args:
        current_letter (str): Літара, якую трэба канвертаваць
        next_letter (str): Папярэдняя літара ў тэксце
        next_next_letter (str): Наступная літара ў тэксце
        miakkasc (bool): Ці пазначаць транзітыўную мяккасць

    Returns:
        str: вынік канвертацыі
    """
    hard, soft = MOHUC_PAZNACZACCA_JAK_MIAKKIJA[current_letter.lower()]
    converted_letter = ""
    if next_letter and next_letter.lower() == "ь":
        converted_letter = soft
    elif (
        next_letter
        and current_letter.lower() == "л"
        and next_letter.lower() in JOTAWANYJA_LITARY
    ):
        converted_letter = soft
    elif (
        next_next_letter
        and current_letter.lower() == next_letter.lower() == "л"
        and (
            next_next_letter.lower() in JOTAWANYJA_LITARY
            or next_next_letter.lower() == "ь"
        )
    ):
        converted_letter = soft
    elif (
        miakkasc
        and next_letter
        and next_next_letter
        and _ci_patrabuje_adlustravannia_tranzityunaj_miakkasci(
            next_letter, next_next_letter
        )
    ):
        if current_letter.lower() != "н" or (
            current_letter.lower() == "н" == next_letter.lower()
        ):
            converted_letter = soft
        else:
            converted_letter = hard
    else:
        converted_letter = hard

    return converted_letter


def _convert(text: str, modern: bool = True, miakkasc: bool = True) -> str:
    """Канвертуе тэкст з кірыліцы да лацінкі. Усе літары і знакі, які не могуць
        лічыцца беларускай кірыліцай захоўваюцца без зменаў.

    Args:
        text (str): Тэкст для канвертацыі
        modern (bool, optional): Ці канвертаваць да сучаснай ("чэшчскай") лацінкі.
            Па змоўчванню True.
        miakkasc (bool, optional): Ці адлюстроўвацць транзітыўную мяккасць. Па змоўчванню True.

    Returns:
        str: Сканвертаваны тэкст
    """
    converted_text = ""
    text_length = len(text)
    biahuczyja_pravily = (
        PRAVILY_KANVERTACYJ if modern else KLASICZNYJA_PRAWILY_KANVERTACYJI
    )

    for index, current_letter in enumerate(text):
        converted_letter = ""
        if index > 0:
            previous_letter = text[index - 1]
        else:
            previous_letter = ""

        if index < text_length - 1:
            next_letter = text[index + 1]
        else:
            next_letter = ""

        if index < text_length - 2:
            next_next_letter = text[index + 2]
        else:
            next_next_letter = ""

        if current_letter.lower() in biahuczyja_pravily:
            converted_letter = biahuczyja_pravily[current_letter.lower()]
        elif current_letter.lower() in MOHUC_PAZNACZACCA_JAK_MIAKKIJA:
            converted_letter = _miakkuja_zycznyja(
                current_letter, next_letter, next_next_letter, miakkasc
            )
        elif current_letter.lower() == "ь" or current_letter.lower() == "'":
            pass
        # Перадаюцца праз i/j
        elif current_letter.lower() in JOTAWANYJA_LITARY:
            converted_letter = _kanvertavac_z_j(current_letter, previous_letter)
        else:
            converted_letter = current_letter

        converted_letter = (
            converted_letter
            if current_letter.islower()
            else converted_letter.capitalize()
        )
        converted_text += converted_letter

    return converted_text


def convert(text: str, miakkasc: bool = True) -> str:
    """Канвертуе з кірыліцы да сучаснай ("чэшскай") лацінкі. Усе літары і знакі, які не могуць
        лічыцца беларускай кірыліцай захоўваюцца без зменаў.


    Args:
        text (str): Тэкст які мусіць быць сканвертаваны
        miakkasc (bool, optional): Ці пазначаць транзітыўную мяккасць.
            Па змоўчванню True.

    Returns:
        str: Вынік канвертацыі
    """
    return _convert(text=text, modern=True, miakkasc=miakkasc)


def convert_old(text: str, miakkasc: bool = True) -> str:
    """Канвертуе з кірыліцы да старой ("польскай") лацінкі. Усе літары і знакі, які не могуць
        лічыцца беларускай кірыліцай захоўваюцца без зменаў.


    Args:
        text (str): Тэкст, які мусіць быць сканвертаваны.
        miakkasc (bool, optional): Ці пазначаць транзітыўную мяккасць.
            Па змоўчваннб True.

    Returns:
        str: Вынік канвертацыі
    """
    return _convert(text=text, modern=False, miakkasc=miakkasc)
