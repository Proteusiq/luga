from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple

from fasttext import FastText, load_model  # type: ignore
from httpx import Client
from numpy.typing import NDArray

__MODEL_PATH = Path(__file__).parent / "models"
__MODEL_FILE = __MODEL_PATH / "language.bin"  # lid.176.bim 128MB model
__MODEL_URL = "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"

if not __MODEL_FILE.exists():
    # print(f"Downloading language model from {__MODEL_URL!r}. Runs only once!")
    __MODEL_PATH.mkdir(exist_ok=True)
    with Client() as client, __MODEL_FILE.open("wb") as f:
        model_content = client.get(__MODEL_URL)
        f.write(model_content.content)
    # print("Downloading completed!")


# mute warning with eprint
# Warning : `load_model` does not return WordVectorModel or SupervisedModel
#  any more, but a `FastText` object which is very similar.
FastText.eprint = lambda x: None
fmodel = load_model(f"{__MODEL_FILE}")


@dataclass(frozen=True)
class Language:
    name: str = field(default="unknown", metadata={"language": "predicted language"})
    score: float = field(
        default=0.0, metadata={"trustability": "probability of prediction"}
    )


def beautify_one(
    response: Tuple[str, NDArray], threshold: Optional[float] = 0.5
) -> Language:

    score_: NDArray
    language, score_ = response
    # (('__label__da',), array([0.99840873]))
    score = score_.squeeze().item()

    if score < threshold:
        return Language()

    return Language(name=language[0].replace("__label__", ""), score=score)


def beautify_many(
    responses: Tuple[str, NDArray], threshold: Optional[float] = 0.5
) -> List[Language]:

    # ([['__label__da'], ['__label__en']],
    # [array([0.99840873], dtype=float32), array([0.9827167], dtype=float32)])

    languages, scores = responses
    results = []
    for lang, score_ in zip(languages, scores):
        score = score_.squeeze().item()

        if score < threshold:
            results.append(Language())
            
        else:
            results.append(Language(name=lang[0].replace("__label__", ""), score=score))

    return results
