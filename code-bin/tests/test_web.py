import unittest

from webtest import TestApp
from main import application


class WebTest(unittest.TestCase):
    def setUp(self):
        self.app = TestApp(application())

    def test_index(self):
        response = self.app.get('/')
        assert 'Hello world!' in str(response)

