Luga
==============================
- A blazing fast language detection using fastText's language models

_Luga_ is a Swahili word for language. [fastText](https://github.com/facebookresearch/fastText) provides blazing-fast
language detection tool. Lamentably, [fastText's](https://fasttext.cc/docs/en/support.html) API is beauty-less and the documentation is a bit fuzzy.
It is also funky that we have to manually [download](https://fasttext.cc/docs/en/language-identification.html) and load models.

Here is where _luga_ comes in. We abstract unnecessary steps and allow you to do precisely one thing: detecting text language.


### Installation
```bash
python -m pip install -U luga
```

### Usage:
⚠️ Note: The first usage downloads the model for you. It will take a bit longer to import depending on internet speed.
It is done only once.

```python
from luga import language

print(language("the world has ended yesterday"))

# Language(name='en', score=0.9804665446281433)
```

### Without Luga:

Download the model
```bash
wget https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin -O /tmp/lid.176.bin
```

Load and use
```python
import fasttext

PATH_TO_MODEL = '/tmp/lid.176.bin'
fmodel = fasttext.load_model(PATH_TO_MODEL)
fmodel.predict(["the world has ended yesterday"])

# ([['__label__en']], [array([0.98046654], dtype=float32)])
```
### Comming soon ...


### Dev:

```bash
poetry run pre-commit install
```

#### TODO:
- [ ] refactor artifacts.py
- [ ] auto checkers with pre-commit | invoke
- [ ] write more tests
- [ ] write github actions
- [ ] create a smart data checker (a fast List[str], what do with none strings)
- [ ] make it faster with Cython
