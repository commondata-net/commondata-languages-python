# commondata-languages

Work with [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1), [ISO 639-2B, ISO 639-2T](https://en.wikipedia.org/wiki/ISO_639-2), and [ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3) language data.

List, lookup with fuzzy search.

## Installation

```bash
pip install commondata-languages
```

## Usage

**Iterate over all languages:**

```python
from commondata_languages import LanguageData

languages = LanguageData()

for language in languages:
    print(language.name)
```

**List all languages:**

```python
from commondata_languages import LanguageData

languages = LanguageData()

print(languages.all())
```

**Lookup a language**

```python
from commondata_languages import LanguageData

languages = LanguageData()

# Lookup by name (case insensitive, fuzzy search)
language = languages["Hindi"]

# Lookup by ISO 639-1
language = languages["en"]

# Lookup by ISO 639-3
language = languages["eng"]

# Lookup by ISO 639-2B
language = languages["chi"]

# Lookup by ISO 639-2T
language = languages["zho"]

# Look up with fuzzy search
language = languages["Englih"]

print(language)
> Language(name='English', iso1='en', iso2b='eng', iso2t='eng', iso3='eng', scope='Individual', type='Living')
```

**Use CLI to lookup a language**

```bash
python -m commondata-languages English
```

**Load languages data into pandas dataframe**

```python
import pandas as pd

from commondata_languages.data import languages

df = pd.DataFrame(languages)
```

## Other Formats and Datasets

Download CSV, XLSX, JSON and YAML files from [commondata.net/languages](https://commondata.net/languages).

[commondata.net](https://commondata.net) maintains a collection of essential datasets in a variety of formats, including
python bindings. Check out the full library here: [commondata.net/library](https://commondata.net/library).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request [here](https://github.com/commondata-net/commondata-languages-python).

## License

This project is licensed under GPLv3. See the [LICENSE](https://github.com/commondata-net/commondata-languages-python/blob/main/LICENSE) file for details.

## Support

For feedback, feature requests, or support, please email [support@commondata.net](mailto:support@commondata.net).
