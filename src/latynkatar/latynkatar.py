from .variables import (
    PRAVILY_KANVERTACYJ,
    HALOSNYJA,
    PRAVILY_KANVERTACYJ_Z_J,
    MOHUC_PAZNACZACCA_JAK_MIAKKIJA,
)


class Cyr2Lat:
    @classmethod
    def convert(cls, text: str) -> str:
        converted_text = ""
        text_length = len(text)
        for index in range(text_length):
            if index > 0:
                previous_letter = text[index - 1]
            else:
                previous_letter = None

            current_letter = text[index]
            if index < text_length - 1:
                next_letter = text[index + 1]
            else:
                next_letter = None

            if current_letter.lower() in PRAVILY_KANVERTACYJ:
                converted_letter = PRAVILY_KANVERTACYJ[current_letter.lower()]
                if current_letter.isupper():
                    converted_letter = converted_letter.upper()

                converted_text += converted_letter
            elif current_letter.lower() == "л":
                if next_letter and next_letter.lower() in ("ь",) + tuple(
                    PRAVILY_KANVERTACYJ_Z_J.keys()
                ):
                    converted_text += "l" if current_letter.islower() else "L"
                else:
                    converted_text += "ł" if current_letter.islower() else "Ł"
            # могуць змякчацца асобна ад галосных літар пасля іх (мяккі знак)
            elif current_letter.lower() in MOHUC_PAZNACZACCA_JAK_MIAKKIJA:
                hard, soft = MOHUC_PAZNACZACCA_JAK_MIAKKIJA[current_letter.lower()]
                if next_letter and next_letter.lower() == "ь":
                    converted_text += soft if current_letter.islower() else soft.upper()
                else:
                    converted_text += hard if current_letter.islower() else hard.upper()
            elif current_letter.lower() == "х":
                converted_text += "ch" if current_letter.islower() else "Ch"
            elif current_letter.lower() == "ь" or current_letter.lower() == "'":
                pass
            # Перадаюцца праз i/j
            elif current_letter.lower() in PRAVILY_KANVERTACYJ_Z_J:
                if (
                    not previous_letter
                    or previous_letter.lower() in HALOSNYJA
                    or not previous_letter.isalpha()
                    or previous_letter == "'"
                ) and current_letter.lower() != "і":
                    base = "j" if current_letter.islower() else "J"
                else:
                    base = "i" if current_letter.islower() else "I"

                second_letter = PRAVILY_KANVERTACYJ_Z_J[current_letter.lower()]
                if (
                    current_letter.lower() != "і"
                    and previous_letter
                    and previous_letter.lower() == "л"
                ):
                    converted_letter = (
                        second_letter
                        if current_letter.islower()
                        else second_letter.upper()
                    )
                else:
                    converted_letter = base + second_letter

                converted_text += converted_letter
            else:
                converted_text += current_letter

        return converted_text
