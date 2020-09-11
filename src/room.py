# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
class Room:
    def __init__(self, room, room_desc, room_items = []):
        self.room = room
        self.room_desc = room_desc
        self.room_items = room_items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def search(self):
        if not self.room_items:
            return print(f"You can't see anything worth picking up.")
        else:
            return print(f"You see a {self.room_items}")
        
    def __str__(self):
        output = self.room + ' ' + self.room_desc 

        return output

        # print(output)
