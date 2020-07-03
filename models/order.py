from dataclasses import dataclass
from enum import Enum
from models.base import Model
from models.base import QuerySet
from models.product import Product
from models.user import User
from typing import List


class OrderStatus(Enum):
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELED = "canceled"
    REFUNDED = "refunded"


@dataclass
class Order(Model):
    user_id: str = None
    product_ids: List[str] = None
    status: OrderStatus = None
    # TODO: change to absolute date
    eta: int = None  # days, relative to today

    # FK
    user: User = None
    products: List[Product] = None

    def initialize(self):
        super().initialize()
        if self.user_id is not None:
            self.user = User.get(id=self.user_id)
        if self.product_ids is not None:
            self.products = [
                Product.get(id=product_id) for product_id in self.product_ids
            ]

    @classmethod
    def all(cls) -> QuerySet:
        # avoid circular import
        from db.orders import objects

        qs = QuerySet()
        qs.extend(objects())
        return qs
