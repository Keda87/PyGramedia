import asyncio
import random
import urllib
from typing import List, Optional, Union

from aiohttp import ClientSession

# Reference: https://github.com/tamimibrahim17/List-of-user-agents
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
    'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
    'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
    'Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14',
    'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
    'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0',
    'Mozilla/4.0 (compatible; MSIE 5.23; Mac_PowerPC)',
    'Mozilla/4.0 (compatible; MSIE 5.22; Mac_PowerPC)',
    'Mozilla/4.0 (compatible; MSIE 5.21; Mac_PowerPC)',
    'Mozilla/4.0 (compatible; MSIE 5.2; Mac_PowerPC)',
    'Mozilla/4.0 (compatible; MSIE 5.2; Mac_PowerPC)',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; el-gr) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; ca-es) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-tw) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; ja-jp) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; it-it) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16',
]


class BaseAPI:

    def __init__(self) -> None:
        self.url = None
        self._loop = asyncio.get_event_loop()
        self._base_url = 'https://www.gramedia.com/api'

    @classmethod
    def _build_url(cls, url: str, **kwargs: dict):
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        query_string = urllib.parse.urlencode(kwargs)
        return f'{url}?{query_string}'

    async def _get(self, url: str, **kwargs: dict):
        url = self._build_url(url, **kwargs)
        header = {"User:Agent": random.choice(USER_AGENTS)}
        async with ClientSession() as session:
            async with session.get(url=url, headers=header) as response:
                return await response.json(encoding='utf8')

    async def _post(self, url: str, data: dict):
        header = {"User:Agent": random.choice(USER_AGENTS)}
        async with ClientSession() as session:
            async with session.post(url=url, data=data, headers=header) as response:
                return await response.json(encoding='utf8')

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.url}>'


class ProductAPI(BaseAPI):

    def __init__(self) -> None:
        super(ProductAPI, self).__init__()
        self.url = f'{self._base_url}/products/'

    def retrieve(self,
                 category: Optional[Union[List[str], str]] = None,
                 limit: Optional[int] = None,
                 sync: bool = False):
        coroutine = self._get(
            url=self.url,
            **{'category': category, 'per_page': limit},
        )

        if sync:
            return self._loop.run_until_complete(coroutine)
        return coroutine


class CategoryAPI(BaseAPI):

    def __init__(self) -> None:
        super(CategoryAPI, self).__init__()
        self.url = f'{self._base_url}/categories/'

    def retrieve(self, sync: bool = False):
        coroutine = self._get(url=self.url)
        if sync:
            return self._loop.run_until_complete(coroutine)
        return coroutine


class PyGramedia:

    def __init__(self) -> None:
        self.product = ProductAPI()
        self.category = CategoryAPI()

    def __repr__(self):
        return f'<{self.__class__.__name__}>'

