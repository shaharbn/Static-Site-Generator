import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_same_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_same_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com/")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_same_text(self):
        node = TextNode("This is a text node1", TextType.BOLD)
        node2 = TextNode("This is a text node2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    # New test cases
    def test_same_url(self):
        node = TextNode("Text with URL", TextType.LINK, "https://example.com")
        node2 = TextNode("Text with URL", TextType.LINK, "https://example.com")
        self.assertEqual(node, node2)

    def test_empty_node(self):
        node = TextNode("", TextType.TEXT)
        node2 = TextNode("", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("Representation Test", TextType.ITALIC, "https://example.com")
        self.assertEqual(repr(node), "TextNode(Representation Test, italic, https://example.com)")

    def test_different_text_type_url(self):
        node = TextNode("Node 1", TextType.BOLD, "https://url1.com")
        node2 = TextNode("Node 2", TextType.ITALIC, "https://url2.com")
        self.assertNotEqual(node, node2)

    def test_identical_nodes(self):
        node = TextNode("Identical Node", TextType.CODE, "https://sameurl.com")
        node2 = TextNode("Identical Node", TextType.CODE, "https://sameurl.com")
        self.assertEqual(node, node2)

    def test_text_node_to_html_node(self):
        # Test text type
        text_node = TextNode("Hello world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "")
        self.assertEqual(html_node.value, "Hello world!")

    

if __name__ == "__main__":
    unittest.main()
