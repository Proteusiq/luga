from luga import languages


# use parameterize with different languages
def test_sentences():

    responses = languages(["this is just a simple test", "jeg elsker dig"])

    assert responses[1].name == "da", "language detection failed"
    assert responses[1].score > 0.5, "score went boom!"
