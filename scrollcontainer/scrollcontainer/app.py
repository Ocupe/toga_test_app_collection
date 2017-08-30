import toga
from colosseum import CSS


def build(app):
    box = toga.Box(style=CSS(width=200, padding=20))

    def callback(widget):
        box.style.width = box.style.width + 100
        print(box.style.width)

    for x in range(24):
        box.add(toga.Button('Button_{}'.format(x), on_press=callback))
    btn = toga.Button('Button_{}'.format(1), on_press=callback)
    # box.add(btn)


    scrollcontainer = toga.ScrollContainer()
    scrollcontainer.horizontal = False
    scrollcontainer.horizontal = False
    scrollcontainer.content = box
    return scrollcontainer


def main():
    return toga.App('Test Scrollcontainer', 'org.pybee.helloworld', startup=build)


if __name__ == '__main__':
    app = main()
    app.main_loop()
