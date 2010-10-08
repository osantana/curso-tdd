import unittest

from webtest import TestApp, AppError

from main import application
from codebin import reset_counter


class WebTest(unittest.TestCase):
    def setUp(self):
        self.app = TestApp(application())
        reset_counter()

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

    def test_submit_a_plain_text_snippet_and_verify_formatting(self):
        response = self.app.post('/', {
            'code': "Hello world!",
            'lang': "plain",
        })
        response = response.follow()
        body = response.html.body
        self.assertEquals("Hello world!", body.pre.string)

    def test_getting_an_url_that_does_not_exist(self):
        self.assertRaises(AppError, self.app.get, '/A')

    def test_submit_a_python_snippet_and_verify_formatting(self):
        response = self.app.post('/', {
            'code': 'print "Hello!"',
            'lang': "python",
        })
        response = response.follow()
        body = response.html.body
        code = u'<div class="codehilite"><pre><span class="k">print</span> <span class="s">&quot;Hello!&quot;</span>\n</pre></div>\n'
        self.assertEquals(code, body.string)
