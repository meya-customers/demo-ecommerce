from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.element.field import response_field
from meya.entry import Entry
from models.order import Order
from typing import List


@dataclass
class ListOrdersComponent(Component):
    user_id: str = element_field()

    @dataclass
    class Response:
        result: List[Order] = response_field()

    async def start(self) -> List[Entry]:
        orders = list(Order.filter(user=self.user_id))
        return self.respond(data=self.Response(result=orders))
