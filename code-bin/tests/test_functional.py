import selenium_testcase


class TestCase(selenium_testcase.TestCase):
    def test_get_root(self):
        self.selenium.open("/")
        self.assertEquals("Hello world!", self.selenium.get_body_text())


