class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        final = ""
        for item in self.props.items():
            final += f' {item[0]}="{item[1]}"'
        return final

    def __repr__(self):
        return f"HTMLNode(tag = {tag}, value = {self.value}, children = {self.children}, props = {self.props})"
    