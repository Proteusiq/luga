Luga
==============================
- A blazing fast language detection using fastText's language models

_Luga_ is a Swahili word for language. fastText provides blazing-fast
language detection. It is, though, a bit funky to download and load models.
fastText API is also beauty-less. Here is where _luga_ comes in. We abstract unnecessary steps and allow you to do precisely one thing: detecting text language.


### Installation
```bash
python -m pip install -U luga
```

### Usage:
⚠️ Note: The first usage downloads the model for you. It will take a bit longer to import on first usage. It is done only once.

```python
from luga import language

print(language("the world has ended yesterday"))
```

### Comming soon ...

#### TODO:
- [ ] refactor artifacts.py
- [ ] auto checkers with pre-commit | invoke
- [ ] write more tests
- [ ] write github actions
- [ ] create a smart data checker (a fast List[str], what do with none strings)
- [ ] make it faster with Cython
