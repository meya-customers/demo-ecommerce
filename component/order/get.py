from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.element.field import response_field
from meya.entry import Entry
from models.order import Order
from typing import List
from typing import Optional


@dataclass
class OrderGetComponent(Component):
    order_id: str = element_field()

    @dataclass
    class Response:
        result: Optional[Order] = response_field()

    async def start(self) -> List[Entry]:
        order = Order.get(id=self.order_id)
        return self.respond(data=self.Response(result=order))
