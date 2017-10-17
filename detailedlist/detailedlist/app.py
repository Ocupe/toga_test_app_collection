""" 'DetailedList Test App'
This little program let's you check whether or not your DetailedList implementation is working the right way.
"""

import toga
from colosseum import CSS


def build(app):
    box = toga.Box(style=CSS(flex=1, padding=20))

    def on_select(widget, selection):
        print(widget)
        print(selection)

    def on_refresh(widget):
        print('refreshing this shit!')

    def on_delete(widget, row):
        print('deleting someting', widget, 'row', row)
        print(widget)

    dl = toga.DetailedList(data=['Item 0', 'Item 1', 'Item 2'], on_select=on_select, on_delete=on_delete)
    btn = toga.Button('My Button')

    dl.on_refresh = on_refresh
    dl.data = '1 2 3 4 5 6'.split(' ')

    box.add(dl)
    box.add(btn)
    return dl


def main():
    # This needs to return an object that has a main_loop() method.
    return toga.App('DetailedList Test App', 'org.pybee.button', startup=build)


if __name__ == '__main__':
    main().main_loop()
