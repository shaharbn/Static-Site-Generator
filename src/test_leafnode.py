import unittest
from leafnode import *

class TestLeafNode(unittest.TestCase):
    def test_anchor(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_image(self):
        node = LeafNode("img", "", {"src": "photo.jpg", "alt": "A photo"})
        self.assertEqual(node.to_html(), '<img src="photo.jpg" alt="A photo"></img>')

    def test_paragraph(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')

    def test_div_with_classes(self):
        node = LeafNode("div", "Content", {"class": "container main"})
        self.assertEqual(node.to_html(), '<div class="container main">Content</div>')

    def test_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()

    def test_no_properties(self):
        node = LeafNode("h1", "Title")
        self.assertEqual(node.to_html(), '<h1>Title</h1>')

    def test_empty_properties(self):
        node = LeafNode("span", "Highlighted", {})
        self.assertEqual(node.to_html(), '<span>Highlighted</span>')

    def test_special_characters(self):
        node = LeafNode("p", "Hello <world>!")
        self.assertEqual(node.to_html(), '<p>Hello <world>!</p>')

if __name__ == "__main__":
    unittest.main()
