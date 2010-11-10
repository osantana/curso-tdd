from django.test import TestCase

from BeautifulSoup import BeautifulSoup

class WebTest(TestCase):

    def get_html(self, response):
        html = BeautifulSoup(response.content)
        return html

    def test_index(self):
        response = self.client.get("/")
        form = self.get_html(response).form
        self.assertEquals("code", form.textarea.get("name"))
        self.assertEquals("lang", form.select.get("name"))
        self.assertEquals("submit", form.button.get("type"))
        self.assertEquals("Enviar", form.button.string)

    def test_languages(self):
        response = self.client.get("/")
        select = self.get_html(response).form.select
        self.assertEquals("Python",
                select.find(value="python").string)
        self.assertEquals("Ruby",
                select.find(value="ruby").string)
        self.assertEquals("Javascript",
                select.find(value="javascript").string)
        self.assertEquals("HTML",
                select.find(value="html").string)
        self.assertEquals("PHP",
                select.find(value="php").string)
        self.assertEquals("Plain Text",
                select.find(value="plain").string)
