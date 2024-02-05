convertion_rules = {
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
consonants = ("а", "е", "ё", "і", "у", "ы", "э", "ю", "я")
j_based = ("е", "ё", "і", "ю", "я")
j_based_conversion_rules = {
    "е": "e",
    "ё": "o",
    "і": "",
    "ю": "u",
    "я": "a",
}


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

            if current_letter.lower() in convertion_rules:
                converted_letter = convertion_rules[current_letter.lower()]
                if current_letter.isupper():
                    converted_letter = converted_letter.upper()

                converted_text += converted_letter
            elif current_letter.lower() == "л":
                if next_letter and next_letter.lower() in ("ь",) + j_based:
                    converted_text += "l" if current_letter.islower() else "L"
                else:
                    converted_text += "ł" if current_letter.islower() else "Ł"
            elif current_letter.lower() == "н":
                if next_letter and next_letter.lower() == "ь":
                    converted_text += "ń" if current_letter.islower() else "Ń"
                else:
                    converted_text += "n" if current_letter.islower() else "N"
            elif current_letter.lower() == "с":
                if next_letter and next_letter.lower() == "ь":
                    converted_text += "ś" if current_letter.islower() else "Ś"
                else:
                    converted_text += "s" if current_letter.islower() else "S"
            elif current_letter.lower() == "ц":
                if next_letter and next_letter.lower() == "ь":
                    converted_text += "ć" if current_letter.islower() else "Ć"
                else:
                    converted_text += "c" if current_letter.islower() else "C"
            elif current_letter.lower() == "з":
                if next_letter and next_letter.lower() == "ь":
                    converted_text += "ź" if current_letter.islower() else "Ź"
                else:
                    converted_text += "z" if current_letter.islower() else "Z"
            elif current_letter.lower() == "х":
                    converted_text += "ch" if current_letter.islower() else "Ch"
            elif current_letter.lower() == "ь" or current_letter.lower() == "'":
                pass
            # Перадаюцца праз i/j
            elif current_letter.lower() in j_based:
                if (
                    not previous_letter
                    or previous_letter.lower() in consonants
                    or not previous_letter.isalpha()
                    or previous_letter == "'"
                ) and current_letter != "і":
                    base = "j" if current_letter.islower() else "J"
                else:
                    base = "i" if current_letter.islower() else "I"

                second_letter = j_based_conversion_rules[current_letter.lower()]
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
