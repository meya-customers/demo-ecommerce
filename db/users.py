from models.user import User
from typing import List


def objects() -> List[User]:
    _ = list()
    _.append(
        User(
            id="u-12345",
            first_name="Johnny",
            last_name="Rose",
            email="johnny.rose@domain.com",
        )
    )
    _.append(
        User(
            id="u-67890",
            first_name="Stevie",
            last_name="Budd",
            email="stevie.budd@domain.com",
        )
    )
    return _
