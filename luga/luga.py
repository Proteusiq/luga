from typing import List, Optional, Union
from nptyping import NDArray
from luga.artifacts import fmodel, beautify_one, beautify_many, Language


def language(text: str, threshold: Optional[float] = 0.5) -> Language:

    assert isinstance(text, str), f"text ought be type str, we got {type(text)}"

    response = fmodel.predict(text, threshold=threshold)
    return beautify_one(response=response)


def languages(
    texts: List[str],
    threshold: Optional[float] = 0.5,
    only_language: Optional[bool] = False,
    to_array: Optional[bool] = False,
) -> Union[List[Union[str, Language]], NDArray]:

    assert isinstance(
        texts, List
    ), f"text ought be type List[str], we got {type(texts)}"

    responses_ = fmodel.predict(texts, threshold=threshold)
    responses = beautify_many(
        responses=responses_,
        only_language=only_language,
        to_array=to_array,
    )

    return responses
