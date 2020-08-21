from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.element.field import response_field
from meya.entry import Entry
from models.product import Product
from typing import List
from typing import Optional


@dataclass
class ProductGetComponent(Component):
    product_id: str = element_field()

    @dataclass
    class Response:
        result: Optional[Product] = response_field()

    async def start(self) -> List[Entry]:
        self.log.info(f"product_id: {self.product_id}")
        product = Product.get(id=self.product_id)
        return self.respond(data=self.Response(result=product))
