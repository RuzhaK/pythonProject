class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item):
        if self.__capacity > len(self.items):
            self.items.append(item)
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {','.join(self.items)}.\nCapacity left: {self.__capacity - len(self.items)}"


#todo koi test ne minava? probvah no s printirane na parvia primer ne raboti, vapreki primera

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("bottle")
print(inventory.get_capacity())
print(inventory)
