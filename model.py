from dataclasses import dataclass


COLUMNS = [
    {"name": "name", "label": "Name", "field": "name", "required": True},
    {"name": "age", "label": "Age", "field": "age", "sortable": True},
]

GUYS = [
    {"id": 0, "name": "Felle 🍕"},
    {"id": 1, "name": "Hans 📠"},
    {"id": 2, "name": "Scheffler 🐍"},
    {"id": 3, "name": "Thut 🚗"},
    {"id": 4, "name": "Matze 🍆"},
    {"id": 5, "name": "Möhrle 🥕"},
    {"id": 6, "name": "Andi B 🍺"},
    {"id": 7, "name": "Mari 🦊"},
]


@dataclass
class Guy:
    id: int
    name: str


@dataclass
class BBQItem:
    guy: Guy
    name: str
    quantity: int
