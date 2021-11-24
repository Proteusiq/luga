from typing import List, Optional, Union
from luga.artifacts import fmodel, beautify_one, beautify_many, Language


def language(text: str, threshold: Optional[float] = 0.5) -> Language:

    assert isinstance(text, str), f"text ought be type str, we got {type(text)}"

    response = fmodel.predict(text)
    return beautify_one(response=response, threshold=threshold)


def languages(
    texts: List[str],
    threshold: Optional[float] = 0.5,
    only_language: Optional[bool] = False,
) -> Union[List[str], List[Language]]:

    assert isinstance(
        texts, List
    ), f"text ought be type List[str], we got {type(texts)}"

    responses_ = fmodel.predict(texts)
    responses = beautify_many(responses=responses_, threshold=threshold)

    if only_language:
        return [response.name for response in responses]

    return responses
