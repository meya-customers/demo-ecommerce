from dataclasses import dataclass
from meya.button.spec import ButtonSpec
from meya.component.element import Component
from meya.element.field import element_field
from meya.entry import Entry
from meya.orb.composer_spec import ComposerEventSpec
from meya.orb.composer_spec import ComposerVisibility
from meya.tile.event.ask import TileAskEvent
from meya.tile.spec import TileButtonStyle
from meya.tile.spec import TileCell
from meya.tile.spec import TileEventSpec
from meya.tile.spec import TileImage
from meya.tile.spec import TileLayout
from models.order import Order
from typing import List


@dataclass
class OrderDisplayComponent(Component):
    orders: List[Order] = element_field()

    async def start(self) -> List[Entry]:
        tiles = []
        triggers = []
        for order in self.orders:
            button = ButtonSpec(text="Select", result=order.id)
            buttons = self.get_buttons_and_triggers([button])
            triggers += buttons.triggers

            product = order.products[0]
            tile = TileEventSpec(
                title=product.name,
                image=TileImage(url=product.image),
                rows=[
                    [
                        TileCell(
                            cell="Price",
                            value="${:,.2f}".format(product.price),
                        ),
                        TileCell(cell="Status", value=order.status.value),
                    ]
                ],
                buttons=buttons.buttons,
            )
            tiles.append(tile)

        event = TileAskEvent(
            # TODO: move to bot settings
            composer=ComposerEventSpec(visibility=ComposerVisibility.HIDE),
            button_style=TileButtonStyle.TEXT,
            text=None,
            tiles=tiles,
            layout=TileLayout.ROW,
        )
        return self.respond(event, *triggers)
