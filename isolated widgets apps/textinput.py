import time
import toga
from colosseum import CSS


def build(app):
    def on_change(widget):
        print(widget.value)

    def on_submit(widget):
        print(widget.value)

    textinput = toga.TextInput(on_change=on_change, on_submit=on_submit)
    def callback(widget):
        print(textinput.value)
        textinput.value = ''

    btn = toga.Button('Print Value & Clear', on_press=callback)

    box = toga.Box(style=CSS(flex=1, padding=20), children=[textinput, btn])

    return box


if __name__ == '__main__':
    app = toga.App('Test Table', 'org.pybee.helloworld', startup=build)
    app.main_loop()
