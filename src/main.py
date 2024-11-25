from textnode import TextNode, TextType

def main():
    dummy_textnode = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(dummy_textnode)


if __name__ == '__main__':
    main()