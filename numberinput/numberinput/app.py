import toga

import time
import toga
from colosseum import CSS


def build(app):
    box = toga.Box(style=CSS(flex=1, padding=20))
    number_input = toga.NumberInput(min_value=100, max_value=200, step=1)
    box.add(number_input)

    def set_range(widget):
        number_input.range = (0, 10)

    btn = toga.Button('Set Range', on_press=set_range, style=CSS())
    box.add(btn)

    def toggle_enabled(widget):
        number_input.enabled = not number_input.enabled

    toggle_btn = toga.Button('Toggle Enabled', on_press=toggle_enabled)
    box.add(toggle_btn)
    return box


def main():
    return toga.App('Test Slider', 'org.pybee.helloworld', startup=build)


if __name__ == '__main__':
    app = main()
    app.main_loop()
