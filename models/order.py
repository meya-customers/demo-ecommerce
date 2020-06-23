from dataclasses import dataclass
from enum import Enum
from models.base import Model
from models.base import QuerySet
from typing import List


class OrderStatus(Enum):
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELED = "canceled"
    REFUNDED = "refunded"


@dataclass
class Order(Model):
    user: str = None
    products: List[str] = None
    status: OrderStatus = None

    @classmethod
    def all(cls) -> QuerySet:
        # avoid circular import
        from db.orders import objects

        qs = QuerySet()
        qs.extend(objects())
        return qs
