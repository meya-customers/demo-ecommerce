from dataclasses import dataclass
from meya.component.element import Component
from meya.element.field import element_field
from meya.element.field import response_field
from meya.entry import Entry
from models.base import ObjectDoesNotExist
from models.user import User
from typing import List
from typing import Optional


@dataclass
class UserGetComponent(Component):
    user_id: str = element_field()

    @dataclass
    class Response:
        result: Optional[User] = response_field()

    async def start(self) -> List[Entry]:
        try:
            user = User.get(id=self.user_id)
        except ObjectDoesNotExist:
            user = None
        return self.respond(data=self.Response(result=user))
