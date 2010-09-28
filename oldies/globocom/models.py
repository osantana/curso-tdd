class QuantityError(Exception): pass

class Inventory(object):
    def __init__(self):
        self.inventory = {}

    def add(self, name, qty):
        self.inventory[name] = self.get(name) + qty

        return self

    def get(self, name):
        return self.inventory.get(name, 0)

    def remove(self, name, qty):
        if self.get(name) < qty:
            raise QuantityError()

        self.inventory[name] = self.get(name) - qty

        return self


class Order(object):
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty
        self.filled = False

    def fill(self, inventory):
        try:
            inventory.remove(self.name, self.qty)
            self.filled = True
        except QuantityError:
            pass

