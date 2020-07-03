from dataclasses import dataclass
from models.base import Model
from models.base import QuerySet
from numbers import Real


@dataclass
class Product(Model):
    name: str = None
    price: Real = None
    image: str = None

    @classmethod
    def all(cls) -> QuerySet:
        # avoid circular import
        from db.products import objects

        qs = QuerySet()
        qs.extend(objects())
        return qs
