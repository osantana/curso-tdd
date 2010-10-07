import unittest

from codebin import Snippet, reset_counter, get_count

class SnippetTest(unittest.TestCase):
    def setUp(self):
        reset_counter()

    def test_create_basic_snippet(self):
        snippet = Snippet(code="Hello world!", lang="plain")
        self.assertEquals("Hello world!", snippet.code)
        self.assertEquals("plain", snippet.lang)

    def test_snippet_and_generate_short_url(self):
        snippet1 = Snippet(code="Hello world! #1", lang="plain")
        snippet1.generate_short_url()
        self.assertEquals("A", snippet1.url)

    def test_two_snippets_and_generate_short_url(self):
        snippet1 = Snippet(code="Hello world! #1", lang="plain")
        snippet1.generate_short_url()
        self.assertEquals("A", snippet1.url)

        snippet2 = Snippet(code="Hello world! #2", lang="plain")
        snippet2.generate_short_url()
        self.assertEquals("B", snippet2.url)
