# Etranslate

[![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![PyPI version](https://badge.fury.io/py/etranslate.svg)](https://badge.fury.io/py/etranslate)

**Etranslate** is a **free** and **unlimited** python library for translating your texts 

## Install it

```shell
#to install:
pip install etranslate

# to upgrade:
pip install etranslate -U

```

## Features
-  Fast and reliable - it uses `Google translate`
-  Auto language detection
-  Bulk translations


## Use it

The quality from this service is not as good as web google translate. There is nothing we can do about it.

It's unclear whether your ip will be blocked if you relentlessly use the service. Please feedback should you find out any information.

```python
from etranslate import translate

# Translate to English by default
translate("Hallo Welt!")  # 'Hello world!'

translate("Hello world!", to="fa")  # '!سلام دنیا'
translate("Hello world!", to="de")  # 'Hallo Welt!'
translate("Hello world!", src="en", to="fa")  # '!سلام دنیا'

# Detect the language of texts
detect_laguage("Hello world!")  # 'en'
detect_laguage("سلام دنیا")      # 'fa'
```

## Requirements

```
Python >=3.7
requests
```


## Disclaimer

``Etranslate`` makes use of a translate interface floating around the net and is for study and research purpose only.

 The interface may become invalid without notice, which would render ``Etranslate`` completely useless.

## Licenses

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ixabolfazl/etranslate/LICENSE) file for details
