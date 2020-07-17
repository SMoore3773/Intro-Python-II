
class Item:
    def __init__(self, item_name, item_desc):
        self.item_name = item_name
        self.item_desc = item_desc

    def on_take():
        print(f"You have picked up {self.name}!")
    
    def on_drop():
        print(f"You have dropped {self.name}.")

    def __str__(self):
        output = self.item_name + self.item_desc
        return output
