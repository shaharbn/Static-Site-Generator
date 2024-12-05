from text_node import *
from extract_links import *
"""
this class split an raw markdown text to TextNode objects
old_nodes its list of TextNode
delimiter its string that represent how to split the string
text_type its the enum TextType from text_node
"""
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    final_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # Add the non-text type node as is
            final_nodes.append(TextNode(node.text, node.text_type, node.url))
        else:
            # Check if the delimiter count is not even, raise an exception
            if node.text.count(delimiter) % 2 != 0:
                raise Exception("invalid Markdown syntax")
            else:
                nodes = []
                # Split text based on the delimiter
                split_text = node.text.split(delimiter)
                
                # Iterate over each part of the split text
                for idx, text in enumerate(split_text):
                    if idx % 2 == 0:
                        # Even index text parts get TEXT type
                        nodes.append(TextNode(text, TextType.TEXT))
                    else:
                        # Odd index text parts get the passed `text_type`
                        nodes.append(TextNode(text, text_type))
                
                # Add these newly created nodes to the final list
                final_nodes.extend(nodes)
    return final_nodes

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            result.append(node)
        else:
            current_text = node.text
            for link_text, url in links:
                node_split = current_text.split(f"[{link_text}]({url})", 1)
                if node_split[0]:  # Only append if text is not empty
                    result.append(TextNode(node_split[0], TextType.TEXT))
                result.append(TextNode(link_text, TextType.LINK, url))
                current_text = node_split[1]  # Update current_text for next iteration
            if current_text:  # Don't forget remaining text after last link
                result.append(TextNode(current_text, TextType.TEXT))
    return result

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        links = extract_markdown_images(node.text)
        if len(links) == 0:
            result.append(node)
        else:
            current_text = node.text
            for link_text, url in links:
                node_split = current_text.split(f"![{link_text}]({url})", 1)
                if node_split[0]:  # Only append if text is not empty
                    result.append(TextNode(node_split[0], TextType.TEXT))
                result.append(TextNode(link_text, TextType.IMAGE, url))
                current_text = node_split[1]  # Update current_text for next iteration
            if current_text:  # Don't forget remaining text after last link
                result.append(TextNode(current_text, TextType.TEXT))
    return result

