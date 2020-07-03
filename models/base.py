from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from typing import List
from typing import Optional
from uuid import uuid4


def uuid4_hex() -> str:
    return uuid4().hex


class MultipleObjectsReturned(Exception):
    pass


class ObjectDoesNotExist(Exception):
    pass


@dataclass
class Model(ABC):
    OBJECT_PREFIX = ""
    id: str = None

    def __post_init__(self):
        self.initialize()

    def initialize(self):
        if not self.id:
            self.id = self.generate_id()

    def generate_id(self):
        """
        Auto-generate a hex-based id string for the object.
        Can be overridden in sub-class
        """
        if self.OBJECT_PREFIX:
            return f"{self.OBJECT_PREFIX}-{uuid4_hex()}"
        else:
            return uuid4_hex()

    @classmethod
    @abstractmethod
    def all(cls) -> "QuerySet":
        pass

    @classmethod
    def filter(cls, **kwargs) -> "QuerySet":
        return cls.all().filter(**kwargs)

    @classmethod
    def get(cls, **kwargs) -> "Model":
        return cls.all().get(**kwargs)

    @classmethod
    def next(cls, model: "Model") -> Optional["Model"]:
        return cls.all().next(model)


class QuerySet:
    """Iterable class for efficiently iterating over a set of models"""

    def __init__(self):
        self._models: List[Model] = list()

    def __iter__(self):
        def generator(queryset: QuerySet):
            for model in queryset._models:
                yield model

        return generator(self)

    def filter(self, **kwargs) -> "QuerySet":
        """
        Iterate over all filter kwargs to test model for match
        Loosely based on Django field lookups: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#id4
        """
        qs = QuerySet()
        for model in self:
            if self.is_match(model, **kwargs):
                qs.add(model)
        return qs

    def next(self, model: Model) -> Optional[Model]:
        idx = self.index_of(model)
        if 0 <= idx < self.count() - 1:
            return self._models[idx + 1]
        else:
            return None

    def index_of(self, model: Model) -> int:
        idx = 0
        for _model in self:
            if self.is_match(_model, id=model.id):
                return idx
            idx += 1
        return -1

    def get(self, **kwargs) -> Model:
        qs = self.filter(**kwargs)
        if qs.exists():
            if qs.count() == 1:
                return qs.first()
            else:
                raise MultipleObjectsReturned
        else:
            raise ObjectDoesNotExist

    @staticmethod
    def is_match(model: Model, **kwargs) -> bool:
        """
        Only supports exact match
        """
        for key, val in kwargs.items():
            # compare the field lookup to actual value
            if not getattr(model, key, None) == val:
                # return on first non-match
                return False
        return True

    def first(self):
        """Return first object in query set or `None`"""
        for model in self:
            return model
        return None

    def exists(self) -> bool:
        """Check for at least one model in the set"""
        # any() won't go beyond the first element if it's True
        return any(True for _ in self)

    def count(self) -> int:
        return len(self._models)

    def extend(self, models: List[Model]):
        self._models.extend(models)

    def add(self, model: Model):
        self._models.append(model)
