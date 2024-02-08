"""
This file is part of Latynkatar.

Latynkatar is free software: you can redistribute it and/or modify it under the
terms of the GNU Lesser General Public License v3 (LGPLv3) as published by the 
Free Software Foundation, either version 3 of the License, or (at your option) 
any later version.

Latynkatar is distributed in the hope that it will be useful, but WITHOUT ANY 
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Lesser General Public License v3 (LGPLv3) for 
more details. In file LICENSE which should came with a package, or look at it
in the repo, see <https://github.com/measles/latynkatar/blob/main/LICENSE>.

You should have received a copy of the GNU Lesser General Public License v3 
(LGPLv3) along with Latynkatar. If not, see <https://www.gnu.org/licenses/>. 

:copyright: (c) 2023, 2024 by Andrej Zacharevicz.
"""

HALOSNYJA = ("а", "е", "ё", "і", "у", "ы", "э", "ю", "я")
MOHUC_PAZNACZACCA_JAK_MIAKKIJA = {
    "н": ("n", "ń"),
    "с": ("s", "ś"),
    "ц": ("c", "ć"),
    "з": ("z", "ź"),
}
PRAVILY_KANVERTACYJ = {
    "а": "a",
    "э": "e",
    "ы": "y",
    "у": "u",
    "ў": "ǔ",
    "б": "b",
    "в": "v",
    "г": "h",
    "ґ": "g",
    "д": "d",
    "ж": "ž",
    "й": "j",
    "к": "k",
    "м": "m",
    "о": "o",
    "п": "p",
    "р": "r",
    "т": "t",
    "ф": "f",
    "ч": "č",
    "ш": "š",
}
PRAVILY_KANVERTACYJ_Z_J = {
    "е": "e",
    "ё": "o",
    "і": "",
    "ю": "u",
    "я": "a",
}
