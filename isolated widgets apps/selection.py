import toga

import time
import toga
from colosseum import CSS


def build(app):
    item_set_1 = ['other selection 1', 'other selection 2', 'other selection 3', 'new item 4']
    item_set_2 = ['selection 1', 'selection 2', 'selection 3']
    selection = toga.Selection(items=['selection 1', 'selection 2', 'selection 3'], style=CSS(margin=20))

    def swap_selection(widget):
        selection.items = item_set_2 if selection.items == item_set_1 else item_set_1

    def get_selection(widget):
        print(selection.value)

    def set_selection(widget):
        selection.value = 'selection 1'

    box = toga.Box(style=CSS(padding=20))
    box.add(selection)
    box.add(toga.Box(children=[toga.Button('Swap Items', on_press=swap_selection),
                               toga.Button('Get Selected Item', on_press=get_selection),
                               toga.Button('Set Selected Item', on_press=set_selection)]))
    return box


if __name__ == '__main__':
    app = toga.App('Test Slider', 'org.pybee.helloworld', startup=build)
    app.main_loop()
