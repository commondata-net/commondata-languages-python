import pytest

from commondata_languages import Language, LanguageData


@pytest.fixture
def language_data():
    return LanguageData()


def test_list_all_languages(language_data):
    languages = language_data.all()
    assert isinstance(languages, list)
    assert len(languages) > 0
    assert isinstance(languages[0], Language)


def test_lookup_by_iso1(language_data):
    language = language_data["en"]
    assert language.name == "English"
    assert language.iso3 == "eng"


def test_lookup_by_iso2b(language_data):
    language = language_data["chi"]
    assert language.name == "Chinese"
    assert language.iso1 == "zh"


def test_lookup_by_iso2t(language_data):
    language = language_data["zho"]
    assert language.name == "Chinese"
    assert language.iso1 == "zh"


def test_lookup_by_iso3(language_data):
    language = language_data["eng"]
    assert language.name == "English"
    assert language.iso1 == "en"


def test_lookup_by_name(language_data):
    language = language_data["Hindi"]
    assert language, None
    assert language.name == "Hindi"
    assert language.iso1 == "hi"


def test_fuzzy_lookup(language_data):
    language = language_data["Englih"]
    assert language.name == "English"
    assert language.iso1 == "en"


def test_iterate_languages(language_data):
    languages = list(language_data)
    assert len(languages) == len(language_data.all())
    assert isinstance(languages[0], Language)


def test_repr_language(language_data):
    language = language_data["English"]
    assert (
        str(language)
        == "Language(name='English', iso1='en', iso2b='eng', iso2t='eng', iso3='eng', scope='Individual', type='Living')"
    )

    language = language_data["Fiji Hindi"]
    assert (
        str(language)
        == "Language(name='Fiji Hindi', iso1=None, iso2b=None, iso2t=None, iso3='hif', scope='Individual', type='Living')"
    )


# def test_invalid_lookup(language_data):
#     with pytest.raises(KeyError):
#         print(language_data["UnknownLanguage"])
