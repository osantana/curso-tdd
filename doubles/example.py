from time import localtime as ltime
from time import strftime as ftime

class TimeProvider(object):
    hour = property(lambda self: ltime().tm_hour)
    minute = property(lambda self: ltime().tm_min)
    period = property(lambda self: ftime("%p", ltime()))

class TimeDisplay(object):
    def __init__(self, provider=None):
        if not provider:
            provider = TimeProvider()
        self._provider = provider

    def get_time_as_html(self):
        p = self._provider
        ret = "<span>"
        if p.hour == 0 and p.minute <= 1:
            ret += "Midnight"
        elif p.hour == 12 and p.minute <= 1:
            ret += "Noon"
        else:
            ret += "%02d:%02d %s" % (p.hour, p.minute, p.period)
        return ret + "</span>"

import unittest

class DisplayTest(unittest.TestCase):
    def test_display_current_time_at_midnight(self):
        sut = TimeDisplay() # setup
        result = sut.get_time_as_html() # exercise SUT
        self.assertEquals('<span>Midnight</span>', result) # verify

    def test_display_current_time_at_noon(self):
        sut = TimeDisplay() # setup
        result = sut.get_time_as_html() # exercise SUT
        self.assertEquals('<span>Noon</span>', result) # verify

    def test_display_current_time_whenever(self):
        sut = TimeDisplay() # setup
        result = sut.get_time_as_html() # exercise SUT
        self.assertEquals('<span>02:30 AM</span>', result) # verify

