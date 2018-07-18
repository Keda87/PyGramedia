# PyGramedia
Unofficial API wrapper for [Gramedia](https://www.gramedia.com/), the biggest bookstore in Indonesia.

#### Usage:

```python
from pygramed import PyGramedia

obj = PyGramedia()
obj.product.retrieve()
obj.product.retrieve(limit=5)
obj.product.retrieve(limit=10, category='keluarga')
```

#### TODO:
- [x] Product API
- [ ] Category API
- [ ] Reverse engineer another API ?
- [ ] Adding test
- [ ] TravisCI
- [ ] Setup script
