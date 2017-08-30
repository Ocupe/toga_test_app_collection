import toga

import time
import toga
from colosseum import CSS


def build(app):
    box = toga.Box(style=CSS(flex=1, padding=20))
    nuber_input = toga.NumberInput(min_value=100, max_value=200, step=1)
    box.add(nuber_input)

    def callback(widget):
        nuber_input.range = (0, 10)

    btn = toga.Button('Set Range', on_press=callback, style=CSS())
    box.add(btn)

    return box


def main():
    return toga.App('Test Slider', 'org.pybee.helloworld', startup=build)


if __name__ == '__main__':
    app = main()
    app.main_loop()
