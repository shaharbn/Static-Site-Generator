class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("you need to implement to method")
    
    def props_to_html(self):
        final = ''
        for key, value in self.props.items():
            final += f' {key}="{value}"'
        return final
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"