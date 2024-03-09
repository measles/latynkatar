# Łatynkatar

[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://github.com/measles/latynkatar/blob/main/LICENSE)

Маленькая і простая бібліятэка для канвертацыі кірыліцы ў сучасную (з č, š, ǔ) лацінку.

## Усталёўка

Latynkatar [ёсць у PyPI](https://pypi.org/project/latynkatar/).

```console
$ python -m pip install latynkatar
```

Не правяралася і не гарантуецца праца з **Python** да версіі **3.8**.

## Ужыванне

Усё досыць просталінейна:

```python
>>> from latynkatar import Cyr2Lat
>>> Cyr2Lat.convert("Але лёс склаўся так, што хрусць - і папалам!")
'Ale los skłaǔsia tak, što chrusć - i papałam!'
```
Ніякіх зменаў правапісу ці выпраўлення памылак. Кірылічныя сімвалы, якім адпавядае некалькі лацінскіх сімвалаў пры трансляцыі вялікіх літар маюць вялікай толькі першую літару ў пары (Chleb, Jan), што можа быць праблемай у выпадках, калі гэта не слова з вялікай літары ці абрэвіятура, а проста нешта напісане КАПСАМ. Бо атрымаецца ChLEB, JaN.

## Анлайн канвертар
У якасці узору ужывання бібліятэкі ці анлайн канвертэра створанага на яе аснове магу прапанаваць паглядзець на сайт [latynkatar.org](https://latynkatar.org). Зыходнікі даступныя [тут](https://github.com/measles/latynkatar_site).

## Ліцэнзія
Copyright Andrej Zacharevicz, 2023

[![LGPL v3.0](https://www.gnu.org/graphics/lgplv3-with-text-154x68.png)](https://github.com/measles/latynkatar/blob/main/LICENSE) ад [GNU](https://www.gnu.org/licenses/lgpl-3.0.html)