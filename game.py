#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
max_weight = 4


def list_of_items(items):
    
    store_string = ""
    for value in items:
        if value == items[-1]:
            store_string = store_string + value["name"]
            break
        store_string = store_string + value['name'] + ", "
    return store_string



def print_room_items(room):
    
    items_to_print = list_of_items(room["items"])
    if items_to_print:
        print("There is " + items_to_print + " here.")
        print("")


def print_inventory_items(items):
    
    store_string = ""
    for value in items:
        if value == items[-1]:
            store_string = store_string + value["name"] + ".\n"
            break
        store_string = store_string + value["name"] + ", "
    print("You have " + store_string)


def print_room(room):
    
    global karma
    # Display room name
    print()
    print(room["name"].upper())
    print()

    # Display room description
    print(room["description"])
    print()
    # Display the room items
    print_room_items(room)    

def exit_leads_to(exits, direction):
    
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    
    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits, room_items, inv_items):
    
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")
    for item in inv_items:
        print("DROP " + item["id"].upper() + " to drop your " + item["name"] +". ")
        print()
    print("You are carrying this much: " + str(round(mass, 2)) + "kg")    
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    
    return chosen_exit in exits


def execute_go(direction):
    
    global current_room
    exit = is_valid_exit(current_room["exits"], direction)
    if exit:
        current_room = move(current_room["exits"], direction)
    else:
        print("You cannot go there.")


def execute_take(item_id):
    
    global current_room
    global inventory
    global items
    global mass

    try:
        item_in_room = items[item_id]
        if (mass + item_in_room["mass"]) > max_weight:
            print("You cannot carry that much")

        else:
            if current_room["items"]:
                items_lst = current_room["items"]

                if item_in_room not in items_lst:
                    print("You cannot take this")

                for item in items_lst:
                    if item == item_in_room:
                        inventory.append(item)
                        current_room["items"].remove(item)
                        mass += item_in_room["mass"]

    except KeyError:
        print("I don't understand")


def execute_drop(item_id):
    
    global current_room
    global inventory
    global mass

    try:
        item_to_drop = items[item_id]
        if mass < 0:
            print("You cannot drop that much")

        else:
            if inventory:
                inv_lst = inventory

                if item_to_drop not in inventory:
                    print("You cannot drop this")

                for item in inv_lst:
                    if item == item_to_drop:
                        current_room["items"].append(item)
                        inventory.remove(item)
                        mass -= item_to_drop["mass"]

            else:
                print("You cannot drop that.")
    except KeyError:
        print("I don't quite understand")


def execute_command(command):
    
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")


    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    
    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    
    # Next room to go to
    return rooms[exits[direction]]


# This is the entry point of our program
def main():

    # Main game loop
    while True:
        if (items["seal"] in rooms["Throne"]["items"]) and (items["clothes"] in rooms["Kitchen"]["items"]) and (items["food"] in rooms["Throne"]["items"]) and (items["sheets"] in rooms["Bedroom"]["items"]):
            print("CONGRATS! You have won the GAME!!")
            break
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
