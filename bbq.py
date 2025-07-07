from nicegui import ui

import model


class BBQ:
    _orders: list[dict] = []
    _overview: ui.aggrid = None

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
                    # Clear input fields
                    guy.set_value(None),
                    item.set_value(None),
                    quantity.set_value(None),
                ),
            )
        self._overview = ui.aggrid(
            {
                "defaultColDef": {"flex": 1},
                "columnDefs": model.COLUMNS,
                "rowData": self._orders,
            }
        ).classes("w-full ag-theme-balham-dark")

    def _add_order(self, order: dict) -> None:
        self._orders.append(order)
        self._overview.update()
