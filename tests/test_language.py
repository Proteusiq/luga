import pytest
from luga import language


text_examples = {
    ("he", "מטאטא חדש מטאטא טוב"),
    ("ar", "يعطيك العافيه"),
    ("ru", "Я вас любил: любовь еще, быть может"),
    ("da", "Jeg har ikke en rød reje"),
    ("de", "Du gehst mir auf den Keks"),
}

text_examples_ids = (lang for lang, _ in text_examples)


@pytest.mark.parametrize("lang, text", text_examples, ids=text_examples_ids)
def test_sentence(lang, text):

    response = language(text)

    assert (
        response.name == lang
    ), f"expeted {lang} language but detected {response.name}"
    assert response.score > 0.5, "score went boom!"


def test_threashold():

    response = language("this is just a simple test", threshold=0.99)

    assert response.name == "unknown", "threshold setting failed"
    assert response.score == 0.0, "score went boom!"
