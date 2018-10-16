from decimal import Decimal as D

from dateutil.parser import parse


class GramediaObject(object):
    def __init__(self, href: str = "", title: str = ""):
        self.href = href
        self.title = title

    @classmethod
    def create_from_json(cls, data):
        return cls(
            href=data.get("href", None),
            title=data.get("title", None)
        )


class Author(GramediaObject):
    pass


class Category(GramediaObject):
    pass


class Shipping(object):
    def __init__(self, width: str = "", height: str = "", length: str = "", weight: str = ""):
        self.width = width
        self.height = height
        self.length = length
        self.weight = weight

    @classmethod
    def create_from_json(cls, data):
        return cls(
            width=data.get("width", None),
            height=data.get("height", None),
            length=data.get("length", None),
            weight=data.get("weight", None)
        )


class Image(object):
    def __init__(self, href: str = ""):
        self.href = href

    def __str__(self):
        return self.href


class Variant(object):
    def __init__(self, warna_tinta: str = ""):
        self.warna_tinta = warna_tinta

    @classmethod
    def create_from_json(cls, data):
        return cls(
            warna_tinta=data.get("Warna Tinta", None)
        )


class Format(GramediaObject):
    def __init__(self, base_price: str = "", href: str = "", images: [Image] = list(), is_allow_insurance: str = "",
                 is_extra_packing: str = "", name: str = "", pre_order_end: str = "", pre_order_start: str = "",
                 promo_id: str = "", promo_percentage: str = "", promo_price: str = "", publish_date: str = "",
                 rel: str = "", sales_end: str = "", sales_start: str = "", shipping: Shipping = Shipping(),
                 sku: str = "",
                 stock_level: int = 0, title: str = "", type: str = "", variant: Variant = None, version: str = "",
                 weight: str = ""):
        super(Format, self).__init__(href, title)
        self.base_pric = base_price
        self.images = images
        self.is_allow_insurance = is_allow_insurance
        self.is_extra_packing = is_extra_packing
        self.name = name
        self.pre_order_end = pre_order_end
        self.pre_order_start = pre_order_start
        self.promo_id = promo_id
        self.promo_percentage = promo_percentage
        self.promo_price = promo_price
        self.publish_date = publish_date
        self.rel = rel
        self.sales_end = sales_end
        self.sales_start = sales_start
        self.shipping = shipping
        self.sku = sku
        self.stock_level = stock_level
        self.type = type
        self.variant = variant
        self.version = version
        self.weight = weight

    @classmethod
    def create_from_json(cls, data):
        shipping = Shipping.create_from_json(data.get('shipping', {}))
        variant = Variant.create_from_json(data.get('variants', {}))
        return cls(
            base_price=D(str(data.get("basePrice"))) if data.get("basePrice") else None,
            href=data.get("href", None),
            images=[Image(i) for i in data.get("images", [])],
            is_allow_insurance=data.get("isAllowInsurance", False),
            is_extra_packing=data.get("isExtraPacking", False),
            name=data.get("name", None),
            pre_order_end=parse(data.get("preOrderEnd")) if data.get("preOrderEnd") else None,
            pre_order_start=parse(data.get("preOrderStart")) if data.get("preOrderEnd") else None,
            promo_id=data.get("promoId", ""),
            promo_percentage=D(str(data.get("promoPercentage"))) if data.get("promoPercentage") else None,
            promo_price=D(str(data.get("promoPrice"))) if data.get("promoPrice") else None,
            publish_date=parse(data.get("publishDate")) if data.get("publishDate") else None,
            rel=data.get("rel", None),
            sales_end=data.get("salesEnd", None),
            sales_start=data.get("salesStart", None),
            shipping=shipping,
            sku=data.get("sku", None),
            stock_level=int(data.get("stockLevel", 0)),
            title=data.get("title", None),
            type=data.get("type", None),
            variant=variant,
            version=data.get("version", None),
            weight=data.get("weight", None)
        )


class Product(object):

    def __init__(self, authors, categories, formats, href: str = "", is_bestseller: str = "", is_new: str = "",
                 is_promo: str = "", name: str = "", tags: str = "", thumbnail: str = ""):
        self.authors = authors
        self.categories = categories
        self.formats = formats
        self.href = href
        self.is_bestseller = is_bestseller
        self.is_new = is_new
        self.is_promo = is_promo
        self.name = name
        self.tags = tags
        self.thumbnail = thumbnail

    @classmethod
    def create_from_json(cls, data):
        authors = [Author.create_from_json(x) for x in data.get('authors', [])]
        categories = [Category.create_from_json(x) for x in data.get('categories', [])]
        formats = [Format.create_from_json(x) for x in data.get('formats', [])]
        return cls(
            authors=authors,
            categories=categories,
            formats=formats,
            href=data.get("href", None),
            is_bestseller=data.get("isBestseller", None),
            is_new=data.get("isNew", None),
            is_promo=data.get("isPromo", None),
            name=data.get("name", None),
            tags=data.get("tags", None),
            thumbnail=data.get("thumbnail", None)
        )
