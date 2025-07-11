import os
import sqlite3


DB_DIR = "/app/data"
DB_NAME = "trailblaze.db"
DB_PATH = os.path.join(DB_DIR, DB_NAME)
TABLE_NAME = "bbq_orders"


def setup_database_and_table() -> None:
    os.makedirs(DB_DIR, exist_ok=True)
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                guy TEXT NOT NULL,
                item TEXT NOT NULL,
                quantity INTEGER NOT NULL
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Failed to create table {TABLE_NAME}: {e}")
    finally:
        if conn:
            conn.close()


def add_order(guy: str, item: str, quantity: int) -> None:
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO {TABLE_NAME} (guy, item, quantity) VALUES (?, ?, ?)",
            (guy, item, quantity),
        )
        conn.commit()
    except sqlite3.Error as e:
        print(f"Failed to create order for ['{guy}', '{item}', '{quantity}']: {e}")
    finally:
        if conn:
            conn.close()


def get_all_orders() -> list[dict]:
    conn = None
    orders: list[dict] = []
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, guy, item, quantity FROM {TABLE_NAME}")

        column_names = [description[0] for description in cursor.description]
        rows = cursor.fetchall()
        for row in rows:
            order_dict = dict(zip(column_names, row))
            orders.append(order_dict)
    except sqlite3.Error as e:
        print(f"Failed to fetch all orders: {e}")
    finally:
        if conn:
            conn.close()
    return orders


def update_order(id: int, new_guy=None, new_item=None, new_quantity=None) -> None:
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        updates = []
        params = []

        if new_guy:
            updates.append("guy = ?")
            params.append(new_guy)
        if new_item:
            updates.append("item = ?")
            params.append(new_item)
        if new_quantity:
            updates.append("quantity = ?")
            params.append(new_quantity)

        if not updates:
            print(f"No updates for record with ID {id}. Cancelling update operation.")
            return

        query = f"UPDATE {TABLE_NAME} SET {', '.join(updates)} WHERE id = ?"
        params.append(id)

        cursor.execute(query, tuple(params))
        conn.commit()
        if cursor.rowcount == 0:
            print(f"Could not find record with the ID {id}")
    except sqlite3.Error as e:
        print(f"Failed to update record with the ID {id}: {e}")
    finally:
        if conn:
            conn.close()


def delete_order(id: int) -> None:
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = ?", (id,))
        conn.commit()
        if cursor.rowcount == 0:
            print(f"Could not find record with the ID {id}")
    except sqlite3.Error as e:
        print(f"Failed to delete record with the ID {id}: {e}")
    finally:
        if conn:
            conn.close()
