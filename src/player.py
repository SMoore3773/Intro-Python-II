# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, cur_room):
        self.cur_room = cur_room
        # self.room_loc = room_loc
        # self.item_inv = item_inv
        # self.alive = alive
