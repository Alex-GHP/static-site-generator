import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_text_node_to_html_node_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        leafnode = LeafNode(None, "This is a text node")
        self.assertEqual(text_node_to_html_node(node), leafnode)
    
    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        leafnode = LeafNode("b", "This is a text node")
        self.assertEqual(text_node_to_html_node(node), leafnode)

    def test_text_node_to_html_node_anchor(self):
        node = TextNode("This is a text node", TextType.LINK, "www.google.com")
        leafnode = LeafNode("a", "This is a text node", {"href": "www.google.com"})
        self.assertEqual(text_node_to_html_node(node), leafnode)

    def test_text_node_to_html_node_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "www.google.com")
        leafnode = LeafNode("img", "", {"src": "www.google.com", "alt": "This is a text node"})
        self.assertEqual(text_node_to_html_node(node), leafnode)

if __name__ == "__main__":
    unittest.main()