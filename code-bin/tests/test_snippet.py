import unittest

from codebin import Snippet

class SnippetTest(unittest.TestCase):
    def test_create_basic_snippet(self):
        snippet = Snippet(code="Hello world!", lang="plain")
        self.assertEquals("Hello world!", snippet.code)
        self.assertEquals("plain", snippet.lang)

    def test_snippet_and_get_short_url(self):
        snippet1 = Snippet(code="Hello world! #1", lang="plain")
        self.assertEquals("A", snippet1.get_short_url())

        snippet2 = Snippet(code="Hello world! #2", lang="plain")
        self.assertEquals("B", snippet2.get_short_url())
