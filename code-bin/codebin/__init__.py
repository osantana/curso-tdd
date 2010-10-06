import os

from google.appengine.ext import webapp
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

class MainHandler(webapp.RequestHandler):
    def get(self):
        template_values = {
            'form': CodeForm(),
        }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        code = self.request.get("code", "")
        template_values = {
            'code': code,
        }
        path = os.path.join(os.path.dirname(__file__), 'code.html')
        self.response.out.write(template.render(path, template_values))
