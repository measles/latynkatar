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
    PRAVILY_KANVERTACYJ_Z_J,
    MOHUC_PAZNACZACCA_JAK_MIAKKIJA,
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

    second_letter = PRAVILY_KANVERTACYJ_Z_J[current_letter.lower()]
    if (
        current_letter.lower() != "і"
        and previous_letter
        and previous_letter.lower() == "л"
    ):
        base = ""

    converted_letter = set_correct_case(base + second_letter, current_letter)

    return converted_letter


def set_correct_case(converted_letter: str, current_letter: str) -> str:
    return (
        converted_letter if current_letter.islower() else converted_letter.capitalize()
    )


class Cyr2Lat:
    @classmethod
    def convert(cls, text: str) -> str:
        converted_text = ""
        text_length = len(text)
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

            if current_letter.lower() in PRAVILY_KANVERTACYJ:
                converted_letter = PRAVILY_KANVERTACYJ[current_letter.lower()]

                converted_letter = set_correct_case(converted_letter, current_letter)
            elif current_letter.lower() == "л":
                if next_letter and next_letter.lower() in ("ь", "л") + tuple(
                    PRAVILY_KANVERTACYJ_Z_J.keys()
                ):
                    converted_letter = set_correct_case("l", current_letter)
                else:
                    converted_letter = set_correct_case("ł", current_letter)
            # могуць змякчацца асобна ад галосных літар пасля іх (мяккі знак)
            elif current_letter.lower() in MOHUC_PAZNACZACCA_JAK_MIAKKIJA:
                hard, soft = MOHUC_PAZNACZACCA_JAK_MIAKKIJA[current_letter.lower()]
                if next_letter and next_letter.lower() == "ь":
                    converted_letter = set_correct_case(soft, current_letter)
                else:
                    converted_letter = set_correct_case(hard, current_letter)
            elif current_letter.lower() == "х":
                converted_letter = set_correct_case("ch", current_letter)
            elif current_letter.lower() == "ь" or current_letter.lower() == "'":
                pass
            # Перадаюцца праз i/j
            elif current_letter.lower() in PRAVILY_KANVERTACYJ_Z_J:
                converted_letter = karvertavac_z_j(current_letter, previous_letter)
            else:
                converted_letter = current_letter

            converted_text += converted_letter

        return converted_text
