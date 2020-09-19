# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []

    def __str__(self):
        output = f"{self.name} you are here: {self.room}. {self.inventory[0].item_name} "
        return output

    def pickup(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)
    
    def carrying(self):
        if len(self.inventory) == 0:
            return "You are carrying nothing"
        output = "You are carrying a "
        if len(self.inventory) == 1:
            output += self.inventory[0].item_name
            return output
        else: 
            for i in self.inventory:
                if i == self.inventory[-1]:
                    output += "and a " + i.item_name
                    if len(self.inventory) == 2:
                        
                        output = output.replace(",","")
                    return output 
                output += i.item_name + ", "