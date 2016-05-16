import urllib
from BeautifulSoup import BeautifulSoup

from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)


class Url(models.Model):
    url = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)

    def fill_title(self):
        if self.title:
            return

        page = urllib.urlopen(self.url)
        content = page.read()
        document = BeautifulSoup(content)
        try:
            self.title = document.title.string
        except AttributeError:
            self.title = ""

    def add_tag(self, tag):
        if not tag:
            return

        tag, created = Tag.objects.get_or_create(name=tag)
        self.tags.add(tag)


    def add_tags_from_string(self, tags_string):
        tags = tags_string.split(",")
        for tag in tags:
            self.add_tag(tag.strip())
