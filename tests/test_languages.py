from luga import languages


def test_sentences(text_examples):

    responses = languages(text_examples["text"])
    pred_langs = [response.name for response in responses]
    pred_scores = [response.score > 0.5 for response in responses]

    assert pred_langs == text_examples["lang"], "language detection failed"
    assert all(pred_scores), "score went boom!"
