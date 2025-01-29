from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)
    leafnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(leafnode.props_to_html())
    htmlnode = HTMLNode("a", "This is a link", None, {"href": "www.boot.dev", "target": "_blank"})
    print(htmlnode.props_to_html())

main()