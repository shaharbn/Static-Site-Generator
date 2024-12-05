"""
this class represent a full html tag and its content
tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
children - A list of HTMLNode objects representing the children of this node
props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
"""
class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        if children == None:
            self.children = []
        else:
            self.children = children
        if props == None:
            self.props = {}
        else:
            self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        final = ""
        for item in self.props.items():
            final += f' {item[0]}="{item[1]}"'
        return final

    def __repr__(self):
        return f"HTMLNode(tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props})"
    