import time
import toga
from colosseum import CSS


def build(app):
    table = toga.Table(['Fist Heading', 'Second Heading'])
    table.insert(None, 'root1', 'value1')
    table.insert(None, 'root2', 'value2')
    table.insert(None, 'root3', 'value3')
    table.insert(0, 'root4', 'value4')

    for _ in range(200):
        table.insert(None, str(_), 'text')

    return table


if __name__ == '__main__':
    app = toga.App('Test Table', 'org.pybee.helloworld', startup=build)
    app.main_loop()
