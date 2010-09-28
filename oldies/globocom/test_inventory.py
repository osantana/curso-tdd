from nose.tools import *
from models import Inventory, QuantityError

def test_get_item_in_inventory():
    inventory = Inventory()
    assert inventory.get("item #1") == 0

def test_add_item_into_inventory():
    inventory = Inventory()
    inventory.add("item #1", 1)
    assert inventory.get("item #1") == 1

def test_add_item_qty_into_inventory():
    inventory = Inventory()
    inventory.add("item #1", 5).add("item #1", 5)
    assert inventory.get("item #1") == 10

@raises(QuantityError)
def test_cannot_remove_item_from_inventory():
    inventory = Inventory()
    inventory.remove("item #1", 3)

def test_remove_item_from_inventory():
    inventory = Inventory()
    inventory.add("item #1", 5).remove("item #1", 3)
    assert inventory.get("item #1") == 2

@raises(QuantityError)
def test_remove_invalid_quantity_inventory():
    inventory = Inventory()
    inventory.add("item #1", 3).remove("item #1", 5)
    assert inventory.get("item #1") == 3

def test_remove_then_add_item_in_inventory():
    inventory = Inventory()
    inventory.add("item #1", 5)
    inventory.remove("item #1", 3).add("item #1", 4)
    assert inventory.get("item #1") == 6
