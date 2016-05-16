from mocker import Mocker
from BeautifulSoup import BeautifulSoup as BS

from django.db import IntegrityError
from django.test import TestCase

from models import Url, Tag
from utils import import_urls_from_delicious, default_opener


OPENER_RESULT = [
    (u'http://example.com/', [u'tag1', u'tag2'], u'Example #1', u"", None),
    (u'http://google.com/', [u'tag1'], u'Example #2', u"", None),
    (u'http://yahoo.com/', [u'tag2'], u'Example #3', u"", None),
]


class SimpleTest(TestCase):
    def test_empty_list(self):
        content = BS(self.client.get("/").content)
        self.assertEquals("Nenhuma URL", content.li.string)

    def test_blank_form(self):
        content = BS(self.client.get("/").content)
        inputs = content.form.findAll("input")
        self.assertEquals("url", dict(inputs[0].attrs)["name"])
        self.assertEquals("title", dict(inputs[1].attrs)["name"])
        self.assertEquals("tags", dict(inputs[2].attrs)["name"])
        self.assertEquals("Add", content.button.string)

    def test_add_url(self):
        content = BS(self.client.post("/", {
            'url': 'http://example.com',
        }, follow=True).content)

        self.assertEquals("Example Web Page", content.findAll("a", {'class': 'title'})[0].string)

    def test_add_url_with_title(self):
        content = BS(self.client.post("/", {
            'url': 'http://example.com',
            'title': 'My title',
        }, follow=True).content)

        self.assertEquals("My title", content.findAll("a", {'class': 'title'})[0].string)

    def test_fail_add_empty_url(self):
        content = BS(self.client.post("/", {
            'url': '',
        }, follow=True).content)

        self.assertEquals("Nenhuma URL", content.li.string)

    def test_fail_add_invalid_url(self):
        content = BS(self.client.post("/", {
            'url': 'fulano@gohorse.com',
        }, follow=True).content)

        self.assertEquals("Nenhuma URL", content.li.string)

    def test_fail_add_url_already_exists(self):
        self.client.post("/", {
            'url': 'http://example.com',
        }, follow=True)

        content = BS(self.client.post("/", {
            'url': 'http://example.com',
        }, follow=True).content)

        self.assertEquals("Example Web Page", content.findAll("a", {'class': 'title'})[0].string)

    def test_add_url_with_tag(self):
        content = BS(self.client.post("/", {
            'url': 'http://example.com',
            'title': 'My title',
            'tags': 'test',
        }, follow=True).content)

        self.assertEquals("test", content.findAll("a", {'class': 'tag'})[0].string)

    def test_add_url_with_tags(self):
        content = BS(self.client.post("/", {
            'url': 'http://example.com',
            'title': 'My title',
            'tags': 'tag1, tag2,tag3 ,tag4 , tag5',
        }, follow=True).content)

        tags = content.li.findAll("a", {'class': 'tag'})
        self.assertEquals("tag1", tags[0].string)
        self.assertEquals("tag2", tags[1].string)
        self.assertEquals("tag3", tags[2].string)
        self.assertEquals("tag4", tags[3].string)
        self.assertEquals("tag5", tags[4].string)

    def test_tag_url(self):
        self.client.post("/", {
            'url': 'http://example.com/',
            'title': 'Example #1',
            'tags': 'tag1',
        }, follow=True)
        self.client.post("/", {
            'url': 'http://google.com/',
            'title': 'Example #2',
            'tags': 'tag1',
        }, follow=True)
        self.client.post("/", {
            'url': 'http://yahoo.com/',
            'title': 'Example #3',
            'tags': 'tag2',
        }, follow=True)

        page = self.client.get("/tag/tag1/")
        self.assertEquals(200, page.status_code)

        content = BS(page.content)
        items = content.findAll("li")
        self.assertEquals(len(items), 2)

        content = BS(self.client.get("/tag/tag2/").content)
        self.assertEquals("Example #3", content.findAll("a", {'class': 'title'})[0].string)

    def test_blank_form_in_tag_page(self):
        self.client.post("/", {
            'url': 'http://example.com/',
            'title': 'Example #1',
            'tags': 'tag1',
        }, follow=True)

        content = BS(self.client.get("/tag/tag1/").content)
        inputs = content.form.findAll("input")
        self.assertEquals("url", dict(inputs[0].attrs)["name"])
        self.assertEquals("title", dict(inputs[1].attrs)["name"])
        self.assertEquals("tags", dict(inputs[2].attrs)["name"])
        self.assertEquals("Add", content.button.string)

    def test_fail_tag_does_not_exists(self):
        page = self.client.get("/tag/tag1/")
        self.assertEquals(404, page.status_code)

    def test_add_url_in_tag_page(self):
        self.client.post("/", {
            'url': 'http://example.com/',
            'title': 'Example #1',
            'tags': 'tag1',
        }, follow=True)

        self.client.post("/tag/tag1/", {
            'url': 'http://google.com/',
            'title': 'Example #2',
        }, follow=True)

        content = BS(self.client.get("/tag/tag1/").content)

        items = content.findAll("a", {'class': 'title'})

        self.assertEquals("Example #1", items[0].string)
        self.assertEquals("Example #2", items[1].string)

    def test_add_url_with_tag_in_tag_page(self):
        self.client.post("/", {
            'url': 'http://example.com/',
            'title': 'Example #1',
            'tags': 'tag1',
        }, follow=True)

        self.client.post("/tag/tag1/", {
            'url': 'http://google.com/',
            'title': 'Example #2',
            'tags': 'tag2',
        }, follow=True)

        content = BS(self.client.get("/tag/tag2/").content)

        items = content.findAll("a", {'class': 'title'})
        self.assertEquals("Example #2", items[0].string)

    def test_fail_empty_tag(self):
        response = self.client.get("/tag//", follow=True)
        self.assertEquals(404, response.status_code)

    def test_remove_url(self):
        response = self.client.post("/", {
            'url': 'http://example.com/',
            'title': 'Example #1',
            'tags': 'tag1',
        }, follow=True)

        content = BS(response.content)

        links = content.findAll("a", {'class': 'remove'})
        self.assertEquals(1, len(links))

        link = dict(links[0].attrs)['href']
        response = self.client.get(link, follow=True)
        self.assertEquals(200, response.status_code)

        content = BS(response.content)
        items = content.findAll("a", {'class': 'remove'})
        self.assertEquals(0, len(items))

    def test_fail_remove_invalid_url(self):
        response = self.client.get("/remove/1/", follow=True)
        self.assertEquals(404, response.status_code)


    def test_import_form(self):
        response = self.client.get("/import/", follow=True)
        self.assertEquals(200, response.status_code)

        content = BS(response.content)
        inputs = content.form.findAll("input")
        self.assertEquals("login", dict(inputs[0].attrs)["name"])
        self.assertEquals("password", dict(inputs[1].attrs)["name"])
        self.assertEquals("Import", content.button.string)

    def test_import_all_urls(self):
        mocker = Mocker()
        DeliciousAPI = mocker.replace("deliciousapi.DeliciousAPI")
        dapi = DeliciousAPI()
        dapi.get_user("test_user", "test_pass")
        mocker.result(OPENER_RESULT)

        mocker.replay()

        response = self.client.post("/import/", {
            'login': 'test_user',
            'password': 'test_pass',
        }, follow=True)
        self.assertRedirects(response, "/")

        content = BS(response.content)
        items = content.findAll("li")
        self.assertEquals(len(items), 3)
        mocker.verify()


class TestUrl(TestCase):
    def setUp(self):
        self.mocker = Mocker()

    def test_create_url(self):
        url = Url(url="http://example.com")
        self.assertEquals(url.url, "http://example.com")

    def test_create_url_with_title(self):
        url = Url(url="http://example.com", title="My Title")
        self.assertEquals(url.title, "My Title")

    def test_get_url_title(self):
        response = self.mocker.mock()
        response.read()
        self.mocker.result("""
            <html>
                <head>
                    <title>Example Web Page</title>
                </head>
            </html>
        """)

        urlopen = self.mocker.replace("urllib.urlopen")
        urlopen("http://example.com")
        self.mocker.result(response)
        self.mocker.replay()

        url = Url(url="http://example.com")
        url.fill_title()
        self.assertEquals(url.title, "Example Web Page")

    def test_get_url_with_no_title(self):
        response = self.mocker.mock()
        response.read()
        self.mocker.result("foo.zip")

        urlopen = self.mocker.replace("urllib.urlopen")
        urlopen("http://example.com/foo.zip")
        self.mocker.result(response)
        self.mocker.replay()

        url = Url(url="http://example.com/foo.zip")
        url.fill_title()
        self.assertEquals(url.title, "")

    def test_fill_title_does_not_override_title(self):
        response = self.mocker.mock()
        response.read()
        self.mocker.result("""
            <html>
                <head>
                    <title>Example Web Page</title>
                </head>
            </html>
        """)

        urlopen = self.mocker.replace("urllib.urlopen")
        urlopen("http://example.com")
        self.mocker.result(response)
        self.mocker.replay()

        url = Url(url="http://example.com", title="My Title")
        url.fill_title()
        self.assertEquals(url.title, "My Title")

    def test_add_url_with_tag(self):
        url = Url(url="http://example.com", title="My Title")
        url.save()

        url.add_tag("test")
        self.assertEquals(len(url.tags.all()), 1)

    def test_add_url_with_tags(self):
        url = Url(url="http://example.com", title="My Title")
        url.save()

        url.add_tags_from_string("tag1, tag2 ,tag3 , tag4,tag5,,,")

        tags = url.tags.order_by("name")

        self.assertEquals(len(tags), 5)
        self.assertEquals(tags[0].name, "tag1")
        self.assertEquals(tags[1].name, "tag2")
        self.assertEquals(tags[2].name, "tag3")
        self.assertEquals(tags[3].name, "tag4")
        self.assertEquals(tags[4].name, "tag5")

    def test_create_two_urls_with_same_tag(self):
        url1 = Url(url="http://example.com/1", title="My Title")
        url1.save()
        url1.add_tags_from_string("tag1")

        url2 = Url(url="http://example.com/2", title="My Title")
        url2.save()
        url2.add_tags_from_string("tag1")

        self.assertEquals(url1.tags.all()[0], url2.tags.all()[0])


class TestTag(TestCase):
    def test_create_tag(self):
        tag = Tag(name="test")
        self.assertEquals(tag.name, "test")

    def test_create_tag_without_name(self):
        tag = Tag(name=None)
        self.assertRaises(IntegrityError, tag.save)

    def test_fail_create_tag_already_exists(self):
        tag = Tag(name="test")
        tag.save()

        tag = Tag(name="test")
        self.assertRaises(IntegrityError, tag.save)



class TestUtils(TestCase):
    def test_import_urls_from_delicious(self):
        mocker = Mocker()
        opener = mocker.mock()
        opener("test_user", "test_pass")
        mocker.result(OPENER_RESULT)

        mocker.replay()
        urls = import_urls_from_delicious("test_user", "test_pass", opener)

        self.assertEquals("http://example.com/", urls[0].url)
        self.assertEquals("http://google.com/", urls[1].url)
        self.assertEquals("http://yahoo.com/", urls[2].url)
        mocker.verify()

    def test_default_opener(self):
        mocker = Mocker()
        DeliciousAPI = mocker.replace("deliciousapi.DeliciousAPI")
        dapi = DeliciousAPI()
        dapi.get_user("test_user", "test_pass")
        mocker.result(OPENER_RESULT)

        mocker.replay()
        default_opener("test_user", "test_pass")
        mocker.verify()
