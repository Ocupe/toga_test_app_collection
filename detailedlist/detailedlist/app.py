""" 'DetailedList Test App'
This little program let's you check whether or not your DetailedList implementation is working the right way.
"""

import toga
from colosseum import CSS


def build(app):
    box = toga.Box(style=CSS(flex=1, padding=20))

    dl = toga.DetailedList(data=['Item 0', 'Item 1', 'Item 2'])
    btn = toga.Button('My Button')

    box.add(dl)
    box.add(btn)
    return box


def main():
    # This needs to return an object that has a main_loop() method.
    return toga.App('DetailedList Test App', 'org.pybee.button', startup=build)


if __name__ == '__main__':
    main().main_loop()
