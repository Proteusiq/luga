import pytest


@pytest.fixture()
def text_examples():
    yield {
        "lang": ["he", "ru", "da", "de"],
        "text": [
            "קפוץ לי",
            "Я вас любил: любовь еще, быть может",
            "Det blæser en halv pelican",
            "Das Blaue vom Himmel versprechen",
        ],
    }
