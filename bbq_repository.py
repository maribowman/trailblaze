import sqlite3

DB_FILE = "trailblaze.db"
TABLE_NAME = "bbq_orders"


def create_table_if_not_exists() -> None:
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
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
        conn = sqlite3.connect(DB_FILE)
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
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, guy, item, quantity FROM {TABLE_NAME}")
        orders = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Failed to fetch all orders: {e}")
    finally:
        if conn:
            conn.close()
    return orders


def update_order(id: int, new_guy=None, new_item=None, new_quantity=None) -> None:
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
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
        conn = sqlite3.connect(DB_FILE)
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
