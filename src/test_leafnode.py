import unittest
from leafnode import *

class TestTextNode(unittest.TestCase):
    def test_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_img(self):
        node = LeafNode("img", "", {"src": "photo.jpg", "alt": "A photo"})
        self.assertEqual(node.to_html(), '<img src="photo.jpg" alt="A photo">')

    def test_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')
