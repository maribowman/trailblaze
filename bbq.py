from nicegui import ui

import model


class BBQ:
    _orders: list[dict] = []
    _overview: ui.column = None

    def __init__(self) -> None:
        with ui.card().classes("w-full"):
            guy = ui.select(
                options=model.GUYS,
                label="Wer?",
            ).classes("w-full")
            item = (
                ui.input(
                    placeholder="Trag hier deinen Shit ein!",
                    label="Was?",
                )
                .classes("w-full")
                .props("clearable")
            )
            quantity = ui.select(
                options=[1, 2, 3, 4, 5],
                label="Wie viel?",
            ).classes("w-full")

            ui.button(
                "Hinzufügen",
                on_click=lambda: (
                    self._add_order(
                        {
                            "guy": guy.value,
                            "item": item.value,
                            "quantity": quantity.value,
                        },
                    ),
                    guy.set_value(None),
                    item.set_value(None),
                    quantity.set_value(None),
                ),
            )
        self._overview = ui.column().classes("w-full")

    def _add_order(self, order: dict) -> None:
        self._orders.append(order)
        self._update_overview()

    def _update_overview(self) -> None:
        self._overview.clear()
        with self._overview:
            with ui.card().classes("w-full"):
                for order in self._orders:
                    with ui.row().classes("w-full"):
                        ui.label(order["guy"])
                        ui.label(order["item"])
                        ui.label(order["quantity"])
