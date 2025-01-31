from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_link

def main():
    node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    print(new_nodes)

main()