# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, room, items):
        self.name = name
        self.room = room
        self.items = items

    def __str__(self):
        output = f"{self.name} you are here: {self.room}. "
        return output
    def take(self, obj):
        self.items.append(obj)
    def inventory(self):
        if len(self.items) != 0:
            return print(self.items)
        else:
            return print("You find only lint and a string in your pocket")
    # def move(dir):
    #     output = self.room.{dir}_to
    #     return output