from models.order import Order
from models.order import OrderStatus
from typing import List


def objects() -> List[Order]:
    _ = list()
    _.append(Order(user="u0", products=["p0"], status=OrderStatus.SHIPPED))
    _.append(Order(user="u0", products=["p1"], status=OrderStatus.PROCESSING))
    return _
