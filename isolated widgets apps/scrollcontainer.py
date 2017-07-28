import toga
from colosseum import CSS

def callback(widget):
    print(widget.layout)

def build(app):
    box = toga.Box(style=CSS(flex=1, padding=30))
    for x in range(24):
        box.add(toga.Button('Button_{}'.format(x), on_press=callback))
    btn = toga.Button('Button_{}'.format(1), on_press=callback)
    # box.add(btn)


    scrollcontainer = toga.ScrollContainer(style=CSS(flex=1))
    scrollcontainer.content = box
    return scrollcontainer


if __name__ == '__main__':
    app = toga.App('Test Scrollcontainer', 'org.pybee.helloworld', startup=build)
    app.main_loop()