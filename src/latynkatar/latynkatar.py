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

:copyright: (c) 2023, 2024 by Andrej Zacharevicz.
"""

from .variables import (
    PRAVILY_KANVERTACYJ,
    HALOSNYJA,
    JOTAWANYJA_LITARY,
    ZYCZNYJA_Z_TRANZITAM,
    MOHUC_PAZNACZACCA_JAK_MIAKKIJA,
    KLASICZNYJA_PRAWILY_KANVERTACYJI,
)


def karvertavac_z_j(current_letter: str, previous_letter: str) -> str:
    if (
        not previous_letter
        or previous_letter.lower() in HALOSNYJA
        or not previous_letter.isalpha()
        or previous_letter == "'"
        or previous_letter.lower() == "ь"
    ) and current_letter.lower() != "і":
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


def convert(text: str, classic: bool = False) -> str:
    converted_text = ""
    text_length = len(text)
    biahuczyja_pravily = (
        KLASICZNYJA_PRAWILY_KANVERTACYJI if classic else PRAVILY_KANVERTACYJ
    )

    for index, current_letter in enumerate(text):
        converted_letter = ""
        if index > 0:
            previous_letter = text[index - 1]
        else:
            previous_letter = None

        if index < text_length - 1:
            next_letter = text[index + 1]
        else:
            next_letter = None

        if index < text_length - 2:
            next_next_letter = text[index + 2]
        else:
            next_next_letter = None

        if current_letter.lower() in biahuczyja_pravily:
            converted_letter = biahuczyja_pravily[current_letter.lower()]
        elif current_letter.lower() in MOHUC_PAZNACZACCA_JAK_MIAKKIJA:
            hard, soft = MOHUC_PAZNACZACCA_JAK_MIAKKIJA[current_letter.lower()]
            if next_letter and next_letter.lower() == "ь":
                converted_letter = soft
            elif (
                next_letter
                and current_letter.lower() == "л"
                and next_letter.lower() in JOTAWANYJA_LITARY.keys()
            ):
                converted_letter = soft
            elif (next_letter and next_letter.lower() in ZYCZNYJA_Z_TRANZITAM) and (
                next_next_letter
                and (
                    next_next_letter.lower() in JOTAWANYJA_LITARY
                    or next_next_letter.lower() == "ь"
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
        elif current_letter.lower() == "ь" or current_letter.lower() == "'":
            pass
        # Перадаюцца праз i/j
        elif current_letter.lower() in JOTAWANYJA_LITARY:
            converted_letter = karvertavac_z_j(current_letter, previous_letter)
        else:
            converted_letter = current_letter

        converted_letter = (
            converted_letter
            if current_letter.islower()
            else converted_letter.capitalize()
        )
        converted_text += converted_letter

    return converted_text


class Cyr2Lat:
    @classmethod
    def convert(cls, text: str) -> str:
        return convert(text=text, classic=False)

    @classmethod
    def convert_classic(cls, text: str) -> str:
        return convert(text=text, classic=True)
