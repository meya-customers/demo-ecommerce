from models.order import Order
from models.order import OrderStatus
from typing import List


def objects() -> List[Order]:
    _ = list()
    _.append(
        Order(
            id="o-1",
            user_id="u-12345",
            product_ids=["p-67890"],
            status=OrderStatus.SHIPPED,
            eta=4,
        )
    )
    _.append(
        Order(
            id="o-2",
            user_id="u-12345",
            product_ids=["p-33333"],
            status=OrderStatus.PROCESSING,
            eta=7,
        )
    )
    _.append(
        Order(
            id="o-3",
            user_id="u-67890",
            product_ids=["p-11111"],
            status=OrderStatus.PROCESSING,
            eta=3,
        )
    )
    _.append(
        Order(
            id="o-4",
            user_id="u-67890",
            product_ids=["p-27182"],
            status=OrderStatus.DELIVERED,
            eta=-1,
        )
    )
    return _
