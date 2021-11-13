Luga
==============================
- A blazing fast language detection using fastText's language models

_Luga_ is a Swahili word for language. fastText provides a blazing fast
language detection. It is though a bit funky to download and load models.
fastText API is also beauty-less. This is why _luga_ was born.


### Installation
```bash
python -m pip install -U luga
```

### Usage:
Note: First usage downloads the model for you. This is done only once.

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