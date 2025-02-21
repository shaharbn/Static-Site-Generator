import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        self.assertEqual(node, node2)
    
    def test_not_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_not_eq3(self):
        node = TextNode("This is a text node1", TextType.BOLD, "www.google.com")
        node2 = TextNode("This is a text node2", TextType.BOLD, "www.google.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()