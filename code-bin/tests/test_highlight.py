import unittest

from codebin import highlight

class HighlightTest(unittest.TestCase):
    def setUp(self):
        self.code = {
            'python': 'print "Hello world!"',
            'plain': 'Hello world!',
        }

    def test_highlight_plain_text(self):
        code = self.code['plain']
        self.assertEquals(code, highlight(code, 'plain'))

    def test_highlight_python(self):
        lang = 'python'
        code = self.code[lang]
        result = u'<div class="codehilite"><pre><span class="k">print</span> <span class="s">&quot;Hello world!&quot;</span>\n</pre></div>\n'
        self.assertEquals(result, highlight(code, lang))
