from models.product import Product
from typing import List


def objects() -> List[Product]:
    _ = list()
    _.append(Product(id="p-12345", name="p", price=1.23, image="url"))
    _.append(Product(id="p-67890", name="p", price=1.23, image="url"))
    _.append(Product(id="p-31415", name="p", price=1.23, image="url"))
    _.append(Product(id="p-27182", name="p", price=1.23, image="url"))
    return _
