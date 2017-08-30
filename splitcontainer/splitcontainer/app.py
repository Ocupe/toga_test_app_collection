import toga
from colosseum import CSS


def callback(widget):
    print(widget.layout)


def build(app):
    content_left = toga.Box(style=CSS(padding=20))
    content_right = toga.Box(style=CSS(padding=20))
    for _ in range(10):
        content_left.add(toga.Button('Button {}'.format(_)))
        content_right.add(toga.Button('Button {}'.format(_)))
    split_container = toga.SplitContainer(content=[content_left, content_right])
    return split_container


def main():
    return toga.App('Test SplitContainer', 'org.pybee.helloworld', startup=build)


if __name__ == '__main__':
    app = main()
    app.main_loop()
