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

    def test_submit_one_snippet(self):
        response = self.app.post('/', {
            'code': "Hello world!",
            'lang': "plain",
        })

        self.assertEquals(301, response.status_int)
        self.assertTrue(response.headers['Location'].endswith("/A"))

    def test_submit_two_snippets(self):
        self.app.post('/', {
            'code': "Hello world! #1",
            'lang': "plain",
        })

        response = self.app.post('/', {
            'code': "Hello world! #2",
            'lang': "plain",
        })

        self.assertEquals(301, response.status_int)
        self.assertTrue(response.headers['Location'].endswith("/B"))
