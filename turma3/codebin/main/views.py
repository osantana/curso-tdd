from django import forms
from django.views.generic.simple import direct_to_template

LANGS = (
    ("python", "Python"),
    ("ruby", "Ruby"),
    ("javascript", "Javascript"),
    ("html", "HTML"),
    ("php", "PHP"),
    ("plain", "Plain Text"),
)

class CodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea())
    lang = forms.ChoiceField(choices=LANGS)

def index(request):
    form = CodeForm()
    return direct_to_template(request, "index.html", {'form': form})
