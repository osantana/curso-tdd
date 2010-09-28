class Order(object):
    def __init__(self, name, qty):
        self.item = name, qty
        self.filled = False

    def fill(self, inventory):
        if inventory.has_inventory(*self.item):
            inventory.remove(*self.item)
            self.filled = True

class Inventory(object):
    def __init__(self):
        self.inventory = {}

    def add(self, name, qty):
        self.inventory[name] = self.inventory.get(name, 0) + qty

    def remove(self, name, qty):
        self.inventory[name] -= qty

    def has_inventory(self, name, qty):
        return name in self.inventory and self.inventory[name] >= qty

    def get(self, name):
        return self.inventory[name]

