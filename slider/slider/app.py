import toga

import time
import toga
from colosseum import CSS


def build(app):
    label = toga.Label(text='Value: ')

    def on_slide(widget):
        label.text = 'Value: ' + str(widget.value)

    slider = toga.Slider(range=(0, 100), default=30, on_slide=on_slide, style=CSS())

    box = toga.Box(style=CSS(padding=20))
    box.add(slider)
    box.add(label)

    def toggle_enable(widget):
        slider.enabled = not slider.enabled

    box.add(toga.Button('Toggle Enabled', on_press=toggle_enable))
    return box


def main():
    return toga.App('Test Slider', 'org.pybee.helloworld', startup=build)


if __name__ == '__main__':
    app = main()
    app.main_loop()
