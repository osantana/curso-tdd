import unittest

from webtest import TestApp

from main import application


class WebTest(unittest.TestCase):
    def setUp(self):
        self.app = TestApp(application())

    def test_index(self):
        response = self.app.get('/')
        form = response.html.form
        self.assertEquals("code", form.find(name="textarea")['name'])
        self.assertEquals("lang", form.find(name="select")['name'])
        self.assertEquals("submit", form.find(name="button")['type'])

    def test_languages(self):
        langs = [ "plain", "python", "ruby", "javascript", "html" ]
        response = self.app.get("/")
        form_langs = []
        for opt in response.html.form.select.findAll():
            form_langs.append(opt['value'])
        self.assertEquals(langs, form_langs)

    def test_submit_plaintext(self):
        response = self.app.post('/', {
            'code': "Hello world!",
            'lang': "plain",
        })

        pre = response.html.pre
        self.assertEquals("Hello world!", pre.string)
