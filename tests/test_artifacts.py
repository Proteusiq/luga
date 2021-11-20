import pytest
from fasttext.FastText import _FastText
from luga import artifacts as art


@pytest.mark.slow()
def test_model_deleter():
    # Access to a protected member
    # pylint: disable=W0212
    response = art.model_deleter(model_file=art.__MODEL_FILE)
    assert response, "model deleting failed"


@pytest.mark.slow()
def test_model_loader():
    # Access to a protected member
    # pylint: disable=W0212
    art.model_loader(model_url=art.__MODEL_URL, re_download=True)
    fmodel = art.load_model(f"{art.__MODEL_FILE}")
    assert isinstance(fmodel, _FastText), "model loading failed"
