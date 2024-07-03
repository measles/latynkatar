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
PRAVILY_KANVERTACYJ = {
    "a": "а",
    "e": "э",
    "y": "ы",
    "u": "у",
    "ŭ": "ў",
    "b": "б",
    "v": "в",
    "h": "г",
    "g": "ґ",
    "d": "д",
    "ž": "ж",
    "k": "к",
    "ł": "л",
    "m": "м",
    "o": "о",
    "p": "п",
    "r": "р",
    "t": "т",
    "f": "ф",
    "č": "ч",
    "š": "ш",
    "n": "н",
    "s": "с",
    "z": "з",
    "ń": "н",
    "ś": "с",
    "ć": "ц",
    "ź": "з",
}
SKLADANYJA_HALOSNYJA = {
    "a": "я",
    "e": "е",
    "o": "ё",
    "u": "ю",
    "i": "і",
}


def convert(text:str, classic:bool = False) -> str:
    classic
    text = list(text)
    converted_text = ""

    while len(text) > 0:
        current_letter = text.pop(0)
        if current_letter.lower() in PRAVILY_KANVERTACYJ:
            converted_letter = PRAVILY_KANVERTACYJ[current_letter.lower()]
            converted_letter = (
                converted_letter
                if current_letter.islower()
                else converted_letter.capitalize()
            )
        elif current_letter.lower() == "l":
            converted_letter = "л" if current_letter.islower() else "Л"

            if text[0] and text[0].lower() in SKLADANYJA_HALOSNYJA:
                druhaja_litara = SKLADANYJA_HALOSNYJA[text[0].lower()]  
                converted_letter += druhaja_litara if text[0].islower() else druhaja_litara.upper()
                text.pop(0)
            else:
                converted_letter += "ь"
        elif current_letter.lower() == "c":
            if text[0] and text[0].lower() == "h":
                converted_letter = "х" if current_letter.islower() else "Х"
                text.pop(0)
            else:
                converted_letter = "ц" if current_letter.islower() else "Ц"

        elif current_letter.lower() in ["i", "j"]:
            if text[0] and text[0].lower() in SKLADANYJA_HALOSNYJA:
                converted_letter = SKLADANYJA_HALOSNYJA[text[0].lower()]
                text.pop(0)
            else:
                converted_letter = "і" if current_letter.lower() == "i" else "й"
            converted_letter = (
            converted_letter
            if current_letter.islower()
            else converted_letter.capitalize()
            )


        else:
            converted_letter = current_letter
            
        converted_text += converted_letter

    return converted_text

        

class Lat2Cyr:
    @classmethod
    def convert(cls, text: str) -> str:
        return convert(text=text, classic=False)
