from items import *

room_reception = {
    "name": "Dark Road",
    "description":
    """An old homeless lady is sat on the edge of a path with a sword. She tells you it is very valuable and was passed down from a long line of ancestors. She is offering it for sale for 100 gold. Do you take it?""",

    "exits": {"south": "Admins", "east": "Tutor", "west": "Parking"},

    "items": [item_biscuits, item_handbook],
    "options": ["Attack her","Buy the sword","Ignore her"]
}

room_admins = {
    "name": "The Highway",
    "description":
    """An old man is trying to cross a 4 lane wide highway ahead of you. """,

    "exits":  {"north": "Reception"},

    "items": [],
    "options": ["help him","ignore him"]
}

room_tutor = {
    "name": "Thief's Lair",
    
    "description":
    """A thief has approached you and is demanding everything you have. He seems a worthy enemy, you are sure you can take him on.""",

    "exits": {"west": "Reception"},

    "items": [],
    "options": ["Run away","Attack him"]
}

room_parking = {
    "name": "castle basement"

    "description":
    """You are in the castle basement, there is a puzzle to solve before you can escape""",

    "exits": {"east": "Office", "south": "Reception"},

    "items": []
}

room_office = {
    "name": "Tired Traveller",
    "description":
    """A wary traveller crosses your path, looking exhausted. Do you give him directions or laugh at him as you walk past? """,

    "exits": {"west": "Parking"},

    "items": [item_pen]
    "options": ["Give help","Leave him"]
}

rooms = {
    "Reception": room_reception,
    "Admins": room_admins,
    "Tutor": room_tutor,
    "Parking": room_parking,
    "Office": room_office
}
