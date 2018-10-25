from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]
mass = items['laptop']['mass'] + items['id']['mass'] + items['money']['mass']
max_weight = 7

# Start game at the reception
current_room = rooms["Reception"]
mass = 2
