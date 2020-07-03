from models.product import Product
from typing import List


def objects() -> List[Product]:
    _ = list()
    _.append(
        Product(
            id="p-12345",
            name="Jordan Max 200",
            price=165,
            image="https://images.prismic.io/meya-website/850367cd-19be-49ba-bdae-f29f5bd7701a_jordan-max-200.png?w=200",
        )
    )
    _.append(
        Product(
            id="p-67890",
            name="Jordan Jumpman 2020",
            price=145,
            image="https://images.prismic.io/meya-website/916f7a08-747e-4944-826d-1111a3f66473_jordan-jumpman-2020.png?w=200",
        )
    )
    _.append(
        Product(
            id="p-31415",
            name="Air Jordan 1 Mid SE",
            price=165,
            image="https://images.prismic.io/meya-website/d56344e9-14bd-44da-96fc-75ea95cc672c_air-jordan-1-mid-se.png?w=200",
        )
    )
    _.append(
        Product(
            id="p-27182",
            name="Jordan ADG",
            price=180,
            image="https://images.prismic.io/meya-website/d2039e5a-2baf-4243-a4fa-6f8ffd9c2a97_jordan-adg.png?w=200",
        )
    )
    _.append(
        Product(
            id="p-11111",
            name="Nike Mercurial Superfly 7",
            price=385,
            image="https://images.prismic.io/meya-website/3bf9180c-7b9a-4908-8cd1-24109c700ae4_nike-mercurial-superfly-7.png?w=200",
        )
    )
    _.append(
        Product(
            id="p-22222",
            name="Premier League Tunnel Vision",
            price=205,
            image="https://images.prismic.io/meya-website/5663c636-9af7-449f-b843-dfe253e5e960_premier-league-tunnel-vision.png?w=200",
        )
    )
    _.append(
        Product(
            id="p-33333",
            name="Nike Academy Team",
            price=60,
            image="https://images.prismic.io/meya-website/7bfbe346-17e6-4d90-962a-61d204466afb_nike-academy-backpack.png?w=200",
        )
    )
    return _
