from selenium import selenium

import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        self.selenium = selenium("localhost", 4444, "*firefox", "http://localhost:8080")
        self.selenium.start()

    def tearDown(self):
        self.selenium.stop()

