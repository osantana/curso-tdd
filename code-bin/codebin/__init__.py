import os

from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template

from django import newforms as forms


LANGS = (
    ('plain', "Plain Text"),
    ('python', "Python"),
    ('ruby', "Ruby"),
    ('javascript', "Javascript"),
    ('html', "HTML"),
)

class CodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea())
    lang = forms.ChoiceField(choices=LANGS)


def short(decimal):
    CHARS = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
             "abcdefghijklmnopqrstuvwxyz"
             "0123456789"
             "!$()*-./:;<>[]^_`{|}")
    base = len(CHARS)

    if decimal == 0:
        return CHARS[0]
    else:
        res = ""
        while decimal > 0:
            res = CHARS[decimal % base] + res
            decimal = decimal // base
        return res

class Snippet(db.Model):
    count = 0
    code = db.TextProperty()
    lang = db.StringProperty(choices=[ x for x, y in LANGS ])

    def get_short_url(self):
        ret = short(Snippet.count)
        Snippet.count += 1
        return ret

class MainHandler(webapp.RequestHandler):
    def get(self):
        template_values = {
            'form': CodeForm(),
        }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        self.redirect("/A", 301)
        # code = self.request.get("code", "")
        # template_values = {
        #     'code': code,
        # }
        # path = os.path.join(os.path.dirname(__file__), 'code.html')
        # self.response.out.write(template.render(path, template_values))
