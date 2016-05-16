from django import forms
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404

from models import Url, Tag
from utils import import_urls_from_delicious


class UrlForm(forms.Form):
    url = forms.URLField(max_length=255, label="URL", verify_exists=True)
    title = forms.CharField(max_length=255, label="Title", required=False)
    tags = forms.CharField(max_length=255, label="Tags", required=False)

class ImportForm(forms.Form):
    login = forms.CharField(max_length=64, label="Login")
    password = forms.CharField(max_length=64, label="Password", widget=forms.PasswordInput())


def index(request, tag=None):
    if tag:
        tag_model = get_object_or_404(Tag, name=tag)
        urls = tag_model.url_set.all()
    else:
        urls = Url.objects.all()

    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            url_data = form.cleaned_data['url']
            title = form.cleaned_data['title']
            tags = form.cleaned_data['tags']
            try:
                url = Url(url=url_data, title=title)
                url.fill_title()
                url.save()
                url.add_tags_from_string(tags)
                if tag:
                    url.add_tag(tag)
            except IntegrityError:
                pass
            return HttpResponseRedirect(request.path)
    else:
        form = UrlForm()

    return render_to_response("index.html", {
            'urls': urls,
            'form': form,
        })

def remove(request, id_url):
    url = get_object_or_404(Url, pk=id_url)
    url.delete()
    return HttpResponseRedirect("/")


def import_urls(request):
    if request.method == "POST":
        form = ImportForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            import_urls_from_delicious(
                form_data['login'],
                form_data['password'],
            )
            return HttpResponseRedirect("/")
    else:
        form = ImportForm()
    return render_to_response("import.html", {
            'form': form,
        })
