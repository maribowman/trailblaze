from nicegui import ui

import bbq_repository as repository
import model


ORDERS: list[dict] = []


@ui.page("/")
def bbq() -> None:
    ui.dark_mode().enable()
    repository.setup_database_and_table()

    overview: ui.aggrid = None

    def refresh_orders() -> None:
        ORDERS.clear()
        ORDERS.extend(repository.get_all_orders())

    def add_order(order: dict) -> None:
        if not order["guy"]:
            ui.notify("Jungeee, WEEER?!")
            return
        if not order["item"]:
            ui.notify("Jungeee, WAAS?!")
            return
        if not order["quantity"]:
            ui.notify("Jungeee, WIE VIIIEEEL?!")
            return

        ui.notify("FETTSACK!")
        repository.add_order(
            guy=order["guy"],
            item=order["item"],
            quantity=order["quantity"],
        )
        refresh_orders()
        overview.update()

    async def delete_order() -> None:
        row = await overview.get_selected_row()
        if row:
            ui.notify(f"{row['id']}: {row['guy']}  {row['item']}")
            repository.delete_order(id=row["id"])
            refresh_orders()
            overview.update()

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

        with ui.row():
            ui.button(
                "Hinzufügen",
                on_click=lambda: (
                    add_order(
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

            ui.button("LÖSCHEN", on_click=lambda: delete_order())

    refresh_orders()
    overview = ui.aggrid(
        {
            "defaultColDef": {"flex": 1},
            "columnDefs": model.COLUMNS,
            "rowData": ORDERS,
            "rowSelection": "single",
        }
    ).classes("w-full ag-theme-balham-dark")
