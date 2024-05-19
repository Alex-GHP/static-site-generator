import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "Click", None, {"href": "www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="www.google.com"')

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node, "<p>Hello World!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()