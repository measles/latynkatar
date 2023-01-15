class Cyr2Lat:
    @classmethod
    def convert(cls, text: str) -> str:
        converted_text = ""
        for index in range(len(text)):
            if text[index].lower() == "л":
                if text[index + 1].lower() in ["я", "е", "ь", "ё", "і", "ю"]:
                    converted_text += "l" if text[index].islower() else "L"
                else:
                    converted_text += "ł" if text[index].islower() else "Ł"
            elif text[index].lower() == "ь":
                if text[index - 1].lower() == "л":
                    pass
            # Галосныя: А, Е, Ё, У, О, Ю, Э, Я, І
            elif text[index].lower() == "а":
                converted_text += "a" if text[index].islower() else "A"
            elif text[index].lower() == "э":
                converted_text += "e" if text[index].islower() else "E"
            elif text[index].lower() == "у":
                converted_text += "u" if text[index].islower() else "U"
            elif text[index].lower() == "о":
                converted_text += "o" if text[index].islower() else "O"
            elif text[index].lower() == "і":
                # TODO: Dadać pierachod u J
                converted_text += "i" if text[index].islower() else "I"
            elif text[index].lower() == "е":
                if text[index - 1].lower() == "л":
                    converted_text += "e" if text[index].islower() else "E"
                else:
                    converted_text += "ie" if text[index].islower() else "Ie"
                    # TODO: Dadać pierachod u J
            elif text[index].lower() == "ё":
                if text[index - 1].lower() == "л":
                    converted_text += "o" if text[index].islower() else "O"
                else:
                    converted_text += "io" if text[index].islower() else "Io"
                    # TODO: Dadać pierachod u J
            elif text[index].lower() == "ю":
                if text[index - 1].lower() == "л":
                    converted_text += "u" if text[index].islower() else "U"
                else:
                    converted_text += "iu" if text[index].islower() else "Iu"
                    # TODO: Dadać pierachod u J
            elif text[index].lower() == "я":
                if text[index - 1].lower() == "л":
                    converted_text += "a" if text[index].islower() else "A"
                else:
                    converted_text += "ia" if text[index].islower() else "Ia"
                    # TODO: Dadać pierachod u J

        return converted_text
