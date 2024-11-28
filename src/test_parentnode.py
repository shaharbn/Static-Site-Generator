import unittest
from parentnode import *
from leafnode import *

class TestParentNode(unittest.TestCase):
    def test_single_child(self):
        child = LeafNode("p", "This is a paragraph.")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), '<div><p>This is a paragraph.</p></div>')

    def test_multiple_children(self):
        child1 = LeafNode("h1", "Title")
        child2 = LeafNode("p", "This is a paragraph.")
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(parent.to_html(), '<div><h1>Title</h1><p>This is a paragraph.</p></div>')

    def test_nested_structure(self):
        child1 = LeafNode("h1", "Title")
        child2 = ParentNode("section", [LeafNode("p", "Nested paragraph.")])
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(parent.to_html(), '<div><h1>Title</h1><section><p>Nested paragraph.</p></section></div>')

    def test_no_tag(self):
        child = LeafNode("p", "This is a paragraph.")
        with self.assertRaises(ValueError):
            parent = ParentNode(None, [child])
            parent.to_html()

    def test_no_children(self):
        with self.assertRaises(ValueError):
            parent = ParentNode("div", [])
            parent.to_html()

    def test_with_properties(self):
        child = LeafNode("p", "Content")
        parent = ParentNode("div", [child], {"class": "container"})
        self.assertEqual(parent.to_html(), '<div class="container"><p>Content</p></div>')

    def test_empty_properties(self):
        child = LeafNode("p", "Content")
        parent = ParentNode("div", [child], {})
        self.assertEqual(parent.to_html(), '<div><p>Content</p></div>')

    def test_special_characters(self):
        child = LeafNode("p", "Special <chars> & \"quotes\"")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), '<div><p>Special <chars> & "quotes"</p></div>')

    def test_mixed_children(self):
        child1 = LeafNode("h1", "Header")
        child2 = ParentNode("section", [LeafNode("p", "Nested paragraph.")])
        child3 = LeafNode("p", "Another paragraph.")
        parent = ParentNode("div", [child1, child2, child3])
        self.assertEqual(
            parent.to_html(),
            '<div><h1>Header</h1><section><p>Nested paragraph.</p></section><p>Another paragraph.</p></div>'
        )

if __name__ == "__main__":
    unittest.main()
