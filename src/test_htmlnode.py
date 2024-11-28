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

    def test_initialization_defaults(self):
        node = HTMLNode()
        # Assert default values
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_all_none(self):
        node = HTMLNode(None, None, None, None)
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_props_to_html(self):
        props = {"class": "intro", "id": "main"}
        node = HTMLNode(props=props)
        props_to_html = node.props_to_html()
        self.assertEqual(props_to_html, ' class="intro" id="main"')

    def test_props_to_html_empty(self):
        node = HTMLNode()
        props_to_html = node.props_to_html()
        self.assertEqual(props_to_html, "")

    def test_repr(self):
        tag = "div"
        value = "Content"
        children = [HTMLNode(tag="p", value="Child paragraph")]
        props = {"class": "container"}
        node = HTMLNode(tag, value, children, props)

        # Assert repr output
        expected_repr = ("HTMLNode(tag = div, value = Content, "
                         "children = [HTMLNode(tag = p, value = Child paragraph, children = [], props = {})], "
                         "props = {'class': 'container'})")
        self.assertEqual(repr(node), expected_repr)

    def test_nested_children(self):
        child1 = HTMLNode(tag="p", value="Child 1")
        child2 = HTMLNode(tag="span", value="Child 2")
        node = HTMLNode(tag="div", children=[child1, child2])

        # Assert children structure
        self.assertEqual(len(node.children), 2)
        self.assertEqual(node.children[0].tag, "p")
        self.assertEqual(node.children[1].tag, "span")

# If this script is executed (rather than imported), run the tests
if __name__ == '__main__':
    unittest.main()
