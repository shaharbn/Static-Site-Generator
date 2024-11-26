import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_initialization(self):
        tag = "p"
        value = "Hello, World!"
        children = []
        props = {"class": "intro"}

        node = HTMLNode(tag, value, children, props)

        # Assert that each attribute is set correctly
        self.assertEqual(node.tag, tag)
        self.assertEqual(node.value, value)
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, props)

    def test_all_none(self):
        node = HTMLNode(None, None, None, None)
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        props = {"class": "intro", "test2": "something"}
        node = HTMLNode(None, None, None, props)
        props_to_html = node.props_to_html()
        self.assertEqual(props_to_html, ' class="intro" test2="something"')

# If this script is executed (rather than imported), run the tests
if __name__ == '__main__':
    unittest.main()