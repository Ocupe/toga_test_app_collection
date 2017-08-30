import time
import toga
from colosseum import CSS


def build(app):
    def callback(widget):
        print(widget.values)

    multi_selection = toga.MultiSelection('Pick multiple if you like:', choices=['item 1', 'item 2', 'item 3'], defaults=[True, False, True], on_select=callback)


    def btn_callback(widget):
        multi_selection.row = not multi_selection.row

    btn = toga.Button('Make row', on_press=btn_callback)
    box = toga.Box(style=CSS(flex=1, padding=20), children=[btn, multi_selection])

    return box


if __name__ == '__main__':
    app = toga.App('Test Table', 'org.pybee.helloworld', startup=build)
    app.main_loop()
