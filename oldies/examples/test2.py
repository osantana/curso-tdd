import unittest
from mocker import MockerTestCase
from models import Inventory, Order

class TestOrder(MockerTestCase):
    def test_order_filled(self):
        # setup data
        inventory = self.mocker.mock()
        order = Order("item #1", 50)

        # setup behaviour
        inventory.has_inventory("item #1", 50)
        self.mocker.result(True)
        inventory.remove("item #1", 50)

        self.mocker.replay()
        order.fill(inventory)

        # verify
        self.mocker.verify()
        self.assertTrue(order.filled())

    def test_order_not_filled(self):
        # setup data
        inventory = self.mocker.mock()
        order = Order("item #1", 51)

        # setup behaviour
        inventory.has_inventory("item #1", 50)
        self.mocker.result(False)

        self.mocker.replay() # exercise
        order.fill(inventory)

        self.mocker.verify() # verify
        self.assertFalse(order.is_filled())

