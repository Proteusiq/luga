from typing import List, Optional
from lunga.artifacts import fmodel, beautify_one, beautify_many, Language


def language(text: str, threshold: Optional[float] = 0.5) -> Language:
    
    assert isinstance(text, str), f"text ought be type str, we got {type(text)}"

    response = fmodel.predict(text)
    return beautify_one(response=response, threshold=threshold)


def languages(texts: List[str], threshold: Optional[float] = 0.5) -> List[Language]:

    assert isinstance(texts, List), f"text ought be type List[str], we got {type(texts)}"
    
    responses = fmodel.predict(texts)
    return beautify_many(responses=responses, threshold=threshold)
