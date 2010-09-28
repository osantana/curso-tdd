import unittest

from models import Inventory, Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.inventory.add("item #1", 50)

    def test_order_filled(self):
        order = Order("item #1", 50)
        order.fill(self.inventory)
        self.assertTrue(order.filled)
        self.assertEquals(0, self.inventory.get("item #1"))

    def test_order_not_filled(self):
        order = Order("item #1", 51)
        order.fill(self.inventory)
        self.assertFalse(order.filled)
        self.assertEquals(50, self.inventory.get("item #1"))

