from items import *

room_hall = {
    "name": "Common Halls",
    "description":
    """Another normal day in the Castle of Orleasia, time to get to work""",

    "exits": {"south": "Kitchen", "east": "Bedroom", "west": "Throne"},

    "items": [item_CleanSheets, item_ToDoList]
}

room_kitchen = {
    "name": "The Kitchen",
    "description":
    """Food is prepared here. Cooked by the finest chefs the country has to offer, for The King.""",

    "exits":  {"north": "Hall"},

    "items": [item_KingsFood]
}

room_bedroom = {
    "name": "Royal Bedchambers",
    
    "description":
    """Your majesty the King sleeps here. Sadly there is no Queen in these trying times, he just occupies himself with the local women, but thats a secret from the public.""",

    "exits": {"west": "Hall"},

    "items": [item_DirtyClothes]
}

room_throne = {
    "name": "Throne Room",

    "description":
    """The king sits here all day talking with nobles and kinghts from all around the 4 seas.""",

    "exits": {"east": "Barracks", "south": "Hall"},

    "items": []
}

room_barracks = {
    "name": "Soldiers Barracks",
    "description":
    """The barracks, as stinky as it always is with all the knights and scribes running around.\nA knight waves you asking about the Kings reply on what to do about a neighbouring kingdom.""",

    "exits": {"west": "Throne"},

    "items": [item_KnightSeal]
}

rooms = {
    "Hall": room_hall,    #was reception
    "Kitchen": room_kitchen,    #was admin
    "Bedroom": room_bedroom,       #was tutor
    "Throne": room_throne,    #was parking
    "Barracks": room_barracks    #was office
    
}
