import pytest

from models.order import Order


@pytest.mark.parametrize(("user_id"), [("u-12345"), ("u-67890")])
def test_get_orders(user_id: str):
    for order in Order.filter(user_id=user_id):
        assert order.user.id == order.user_id
        assert len(order.products) > 0
        assert set(order.product_ids) == {
            product.id for product in order.products
        }
