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



import mocker
class DisplayTest(mocker.MockerTestCase):
    def _get_mock(self, h, m, p="AM"):
        mock = self.mocker.mock()

        mock.hour   # access hour
        self.mocker.count(0, 3); self.mocker.result(h)
        mock.minute # access minute
        self.mocker.count(0, 3); self.mocker.result(m)
        mock.period # access period
        self.mocker.count(0, 3); self.mocker.result(p)

        self.mocker.replay()
        return mock

    def tearDown(self):
        self.mocker.verify()

    def test_display_current_time_at_midnight(self):
        sut = TimeDisplay(self._get_mock(0,0))
        self.assertEquals('<span>Midnight</span>',
                            sut.get_time_as_html())

    def test_display_current_time_at_noon(self):
        sut = TimeDisplay(self._get_mock(12,0))
        self.assertEquals('<span>Noon</span>',
                            sut.get_time_as_html())

    def test_display_current_time_whenever(self):
        sut = TimeDisplay(self._get_mock(2,2))
        self.assertEquals('<span>02:02 AM</span>',
                            sut.get_time_as_html())


