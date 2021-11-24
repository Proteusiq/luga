from luga import languages


def test_sentences(text_examples):

    responses = languages(text_examples["text"])
    pred_langs = [response.name for response in responses]
    pred_scores = [response.score > 0.5 for response in responses]

    assert pred_langs == text_examples["lang"], "language detection failed"
    assert all(pred_scores), "score went boom!"


def test_languages(text_examples):

    responses = languages(
        texts=text_examples["text"], threshold=0.7, only_language=True
    )

    assert responses == text_examples["lang"], "language detection failed"
