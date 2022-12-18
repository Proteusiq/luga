from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import Any, List, Optional, Tuple, Union
from gdown import download
from fasttext import FastText, load_model  # type: ignore
from numpy import array
from nptyping import NDArray


__MODEL_PATH = Path(__file__).parent / "models"
__MODEL_FILE = __MODEL_PATH / "language.bin"  # lid.176.bim 128MB model
__FILE_ID = "1OC7C-eL31hoectGueYl6nfioANrZK2WI"
__MODEL_URL = f"https://drive.google.com/u/0/uc?id={__FILE_ID}&confirm=t"


def model_loader(*, model_url: str, re_download: Optional[bool] = False) -> None:
    """Model Downloader

    Args:
        model_url (str): url link to fasttext language model
        re_download (bool, optional): overides a downloaded model. Defaults to False.
    Returns:
        None
    """

    if not __MODEL_FILE.exists() or re_download:
        # print(f"Downloading language model from {__MODEL_URL!r}. Runs only once!")
        __MODEL_PATH.mkdir(exist_ok=True)

        download(url=model_url, output=__MODEL_FILE.as_posix(), quiet=True)
        # print("Downloading completed!")


def model_deleter(*, model_file: Path = __MODEL_FILE) -> bool:
    """Model Remover

    Args:
        model_file (Path, optional): path to where the model is.
        Defaults to __MODEL_FILE.

    Returns:
        bool: True if deletion was successful, else False
    """

    if not model_file.exists():
        return False

    model_file.unlink()
    return True


@dataclass(frozen=True)
class Language:
    name: str = field(default="unknown", metadata={"language": "predicted language"})
    score: float = field(
        default=0.0, metadata={"trustability": "probability of prediction"}
    )

    @staticmethod
    def keys() -> List[str]:
        return [field.name for field in fields(Language)]

    def __getitem__(self, key: str) -> Union[Any, str, float]:
        item = {"name": self.name, "score": self.score}

        return item.get(key)


def beautify_one(response: Tuple[str, NDArray]) -> Language:

    score_: NDArray
    language, score_ = response
    # (('__label__da',), array([0.99840873]))

    if not score_.size:
        return Language()

    score = score_.round(3).squeeze().item()
    return Language(name=language[0].replace("__label__", ""), score=score)


def beautify_many(
    responses: Tuple[str, NDArray],
    only_language: Optional[bool] = False,
    to_array: Optional[bool] = False,
) -> Union[List[Union[str, Language]], NDArray]:

    # ([['__label__da'], ['__label__en']],
    # [array([0.99840873], dtype=float32), array([0.9827167], dtype=float32)])

    languages, scores = responses
    results = []

    for lang, score_ in zip(languages, scores):
        if not score_.size:
            results.append(Language())
        else:
            score = score_.round(3).squeeze().item()
            results.append(Language(name=lang[0].replace("__label__", ""), score=score))

    # smelly code
    if only_language:
        results = [response.name for response in results]  # type: ignore

    if to_array:
        results = array(results)

    return results


# mute warning with eprint
# Warning : `load_model` does not return WordVectorModel or SupervisedModel
#  any more, but a `FastText` object which is very similar.
# pylint: disable=E1111
FastText.eprint = lambda x: None
model_loader(model_url=__MODEL_URL)
fmodel = load_model(f"{__MODEL_FILE}")
