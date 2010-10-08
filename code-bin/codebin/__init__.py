import os

from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template

from django import newforms as forms


import pygments
import pygments.lexers
import pygments.formatters


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


def highlight(code, lang):
    if lang == 'plain':
        return code

    lexer = pygments.lexers.get_lexer_by_name(lang)
    format = pygments.formatters.HtmlFormatter(cssclass="codehilite")
    res = pygments.highlight(code, lexer, format)
    return res


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

class Counter(db.Model):
    count = db.IntegerProperty(default=0)

def get_count():
    def txn():
        counter = Counter.get_by_key_name("counter")
        if counter is None:
            counter = Counter(key_name="counter")
        else:
            counter.count += 1
        counter.put()

    db.run_in_transaction(txn)
    counter = Counter.get_by_key_name("counter")
    return counter.count

def reset_counter():
    counter = Counter.get_by_key_name("counter")
    if counter is not None:
        counter.delete()

class Snippet(db.Model):
    code = db.TextProperty()
    lang = db.StringProperty(choices=[ x for x, y in LANGS ])
    url = db.StringProperty()

    def generate_short_url(self):
        self.url = short(get_count())

class MainHandler(webapp.RequestHandler):
    def get(self):
        template_values = {
            'form': CodeForm(),
        }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        code = self.request.get("code", "")
        lang = self.request.get("lang", "plain")
        snippet = Snippet(code=code, lang=lang)
        snippet.generate_short_url()
        snippet.put()
        self.redirect(snippet.url, 301)

class ViewSnippetHandler(webapp.RequestHandler):
    def get(self, path):
        try:
            snippet = Snippet.all().filter("url =", path)[0]
        except IndexError:
            self.response.clear()
            self.response.set_status(404)
            self.response.out.write("Unknown Snippet")
            return

        code = highlight(snippet.code, snippet.lang)
        template_values = {'code': code,}
        path = os.path.join(os.path.dirname(__file__), 'code.html')
        self.response.out.write(template.render(path, template_values))
