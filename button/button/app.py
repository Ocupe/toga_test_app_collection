""" 'Button Test App'
This little program let's you check whether or not your button implementation is working the right way.
"""

import toga
from colosseum import CSS


def build(app):
    box = toga.Box(style=CSS(flex=1, padding=20))

    def on_press(widget):
        print('Button: ', widget, ' was pressed!')

    btn = toga.Button('My Button', on_press=on_press)

    def activate(widget):
        btn.enabled = False if btn.enabled else True

    btn_enabled = toga.Button('Enable/Disable Button', on_press=activate)
    box.add(btn)
    box.add(btn_enabled)
    return box


def main():
    # This needs to return an object that has a main_loop() method.
    return toga.App('Button Test App', 'org.pybee.button', startup=build)


if __name__ == '__main__':
    main().main_loop()
