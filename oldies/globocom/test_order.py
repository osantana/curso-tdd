from mocker import Mocker

from nose.tools import *

from models import Order, QuantityError

def test_fill_order():
    order = Order("item #1", 50)

    mocker = Mocker()
    inventory = mocker.mock()
    inventory.remove("item #1", 50)

    mocker.replay()
    order.fill(inventory)

    mocker.verify()
    assert order.filled

def test_order_not_filled():
    order = Order("item #1", 1)

    mocker = Mocker()
    inventory = mocker.mock()
    inventory.remove("item #1", 1)
    mocker.throw(QuantityError)

    mocker.replay()
    order.fill(inventory)

    mocker.verify()
    assert not order.filled

