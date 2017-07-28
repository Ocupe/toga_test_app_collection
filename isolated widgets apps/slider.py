import toga

import time
import toga
from colosseum import CSS


def build(app):
    label = toga.Label(text='Value: ')

    def on_slide(widget):
        label.text = widget.value

    slider = toga.Slider(range=(0, 100), default=30, on_slide=on_slide, style=CSS(flex=1, margin=20))

    box = toga.Box()
    box.add(slider)
    box.add(label)
    return box


if __name__ == '__main__':
    app = toga.App('Test Slider', 'org.pybee.helloworld', startup=build)
    app.main_loop()
