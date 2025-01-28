import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_ok(self):
        node = HTMLNode("a", "This is a link", None, {"href": "www.boot.dev", "target": "_blank"})
        result = 'href="www.boot.dev" target="_blank"'
        self.assertEqual(node.props_to_html(), result)

    def test_props_not_ok(self):
        node = HTMLNode("a", "This is a link", None, {"href": "www.boot.dev", "target": "_blank"})
        result = 'href="www.boot.dev"target="_blank"'
        self.assertNotEqual(node.props_to_html(), result)