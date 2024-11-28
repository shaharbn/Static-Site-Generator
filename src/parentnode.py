from htmlnode import *
from leafnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("All parent nodes must have a tag")
        elif not self.children:
            raise ValueError("All parent nodes must have a children")
        else:
            result = ""
            for child in self.children:
                result += child.to_html()
            props_string = ""
            if self.props is not None:
                props_string = self.props_to_html()
            return f'<{self.tag}{props_string}>{result}</{self.tag}>'