import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "Click", None, {"href": "www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="www.google.com"')

if __name__ == "__main__":
    unittest.main()