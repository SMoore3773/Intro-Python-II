
class Item:
    def __init__(self, item_name, item_desc):
        self.item_name = item_name
        self.item_desc = item_desc

    def on_take(self):
        print(f"You have picked up {self.item_name}!")
    
    def on_drop(self):
        print(f"You have dropped {self.item_name}.")

    def __str__(self):
        output = f"{self.item_name}: {self.item_desc}\n"
        return output
