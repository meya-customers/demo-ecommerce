from models.user import User
from typing import List


def objects() -> List[User]:
    _ = list()
    _.append(
        User(id="u-12345", name="Johnny Rose", email="johnny.rose@domain.com")
    )
    _.append(
        User(id="u-67890", name="Stevie Budd", email="stevie.budd@domain.com")
    )
    return _
