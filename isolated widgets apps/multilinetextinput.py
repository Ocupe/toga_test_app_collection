import toga

import time
import toga
from colosseum import CSS


def build(app):
    box = toga.Box()
    text_input = toga.MultilineTextInput(initial='Test Button,\nsuper cool!', style=CSS(flex=1, margin=20))
    def callback(widget):
        text_input.value = 'New Text'

    def callback_clear(widget):
        text_input.clear()
    btn_1 = toga.Button('Set Text', on_press=callback)
    btn_2 = toga.Button('Clear Text', on_press=callback_clear)
    box.add(text_input)
    box.add(btn_1)
    box.add(btn_2)
    return box


if __name__ == '__main__':
    app = toga.App('Test MultilineTextInput', 'org.pybee.helloworld', startup=build)
    app.main_loop()
