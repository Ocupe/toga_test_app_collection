from random import random

import toga
from colosseum import CSS


def build(app):
    data = []
    for x in range(5):
        data.append([str(x) for x in range(5)])

    def selection_handler(widget, row):
        print('selected row: {}'.format(row))

    table = toga.Table(headings=['heading_{}'.format(x) for x in range(5)],
                       data=data,
                       style=CSS(flex=1),
                       on_select=selection_handler)

    def insert_handler(widget):
        table.data.insert(0, [str(round(random() * 100)) for _ in range(5)])
        table._impl.refresh()
        print('Rows', len(table.data.data))

    def delete_handler(widget):
        if len(table.data.data) > 0:
            table.data.remove(table.data.data[0])
            table._impl.refresh()
        else:
            print('Table is empty!')

    btn_style = CSS(flex=1)
    btn_insert = toga.Button('Insert', on_press=insert_handler, style=btn_style)
    btn_delete = toga.Button('Delete', on_press=delete_handler, style=btn_style)
    btn_box = toga.Box(children=[btn_insert, btn_delete], style=CSS(flex_direction='row'))

    box = toga.Box(children=[table, btn_box], style=CSS(flex=1, flex_direction='column', padding=10))
    return box


def main():
    return toga.App('Test Table', 'org.pybee.helloworld', startup=build)


if __name__ == '__main__':
    app = main()
    app.main_loop()
