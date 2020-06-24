from dataclasses import dataclass
from models.base import Model
from models.base import QuerySet


@dataclass
class User(Model):
    first_name: str = None
    last_name: str = None
    email: str = None

    @classmethod
    def all(cls) -> QuerySet:
        # avoid circular import
        from db.users import objects

        qs = QuerySet()
        qs.extend(objects())
        return qs
