from typing import NamedTuple, AnyStr, List, Union, Optional
import requests


class Author(NamedTuple):
    name: AnyStr
    url: AnyStr


class Category(NamedTuple):
    name: AnyStr
    url: AnyStr


class Catalog(NamedTuple):
    name: AnyStr
    thumbnail: AnyStr
    is_promo: bool
    authors: List[Author]
    categories: List[Category]


class BaseAPI:

    def __init__(self):
        self.get = requests.get
        self.base_url = 'https://www.gramedia.com/api'

    def retrieve(self):
        pass


class ProductAPI(BaseAPI):

    def __init__(self) -> None:
        super(ProductAPI, self).__init__()
        self.base_url += '/products/'
        self.limit = None
        self.category = None

    def _build_url(self) -> AnyStr:
        url = self.base_url
        if self.limit:
            if '?' in url:
                url += f'&per_page={self.limit}'
            else:
                url += f'?per_page={self.limit}'

        if self.category:
            if '?' in url:
                url += f'&category={self.category}'
            else:
                url += f'?category={self.category}'
        return url

    def retrieve(self,
                 category: Optional[Union[List[AnyStr], AnyStr]] = None,
                 limit: Optional[int] = None) -> List[Catalog]:
        self.category = category
        self.limit = limit
        url = self._build_url()

        list_catalog = []
        results = self.get(url=url).json()
        for r in results:
            authors = [Author(
                name=_a.get('title'),
                url=_a.get('href'),
            ) for _a in r.get('authors')]

            categories = [Category(
                name=c.get('title'),
                url=c.get('href'),
            ) for c in r.get('categories')]

            catalog = Catalog(
                name=r.get('name'),
                authors=authors,
                categories=categories,
                is_promo=r.get('isPromo'),
                thumbnail=r.get('thumbnail')
            )
            list_catalog.append(catalog)
        return list_catalog


class PyGramedia:

    def __init__(self) -> None:
        self.product = ProductAPI()
