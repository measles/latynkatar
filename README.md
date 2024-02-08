# Latynkatar

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

## Ліцэнзія

[![LGPL v3.0](https://www.gnu.org/graphics/lgplv3-with-text-154x68.png)](https://github.com/measles/latynkatar/blob/main/LICENSE) ад [GNU](https://www.gnu.org/licenses/lgpl-3.0.html)