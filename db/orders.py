from models.order import Order
from models.order import OrderStatus
from typing import List


def objects() -> List[Order]:
    _ = list()
    _.append(
        Order(
            user_id="u-12345",
            product_ids=["p-67890"],
            status=OrderStatus.SHIPPED,
        )
    )
    _.append(
        Order(
            user_id="u-12345",
            product_ids=["p-33333"],
            status=OrderStatus.PROCESSING,
        )
    )
    _.append(
        Order(
            user_id="u-67890",
            product_ids=["p-11111"],
            status=OrderStatus.SHIPPED,
        )
    )
    _.append(
        Order(
            user_id="u-67890",
            product_ids=["p-27182"],
            status=OrderStatus.DELIVERED,
        )
    )
    return _
