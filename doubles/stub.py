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

class ProviderStub(object):
    def __init__(self, hour, minute, period="AM"):
        self.hour = hour
        self.minute = minute
        self.period = period

class DisplayTest(unittest.TestCase):
    def test_display_current_time_at_midnight(self):
        sut = TimeDisplay(ProviderStub(0,0)) # setup
        self.assertEquals('<span>Midnight</span>', sut.get_time_as_html())

    def test_display_current_time_at_noon(self):
        sut = TimeDisplay(ProviderStub(12,0)) # setup
        self.assertEquals('<span>Noon</span>', sut.get_time_as_html())

    def test_display_current_time_whenever(self):
        sut = TimeDisplay(ProviderStub(2,2)) # setup
        result = sut.get_time_as_html() # exercise SUT
        self.assertEquals('<span>02:02 AM</span>', sut.get_time_as_html())



