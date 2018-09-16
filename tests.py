import unittest

from pygramed import PyGramedia


class PyGramediaTest(unittest.TestCase):

    def setUp(self):
        self.pg = PyGramedia()

    def test_repr_product(self):
        self.assertEqual(str(self.pg.product), '<ProductAPI: https://www.gramedia.com/api/products/>')

    def test_repr_category(self):
        self.assertEqual(str(self.pg.category), '<CategoryAPI: https://www.gramedia.com/api/categories/>')


if __name__ == '__main__':
    unittest.main()
