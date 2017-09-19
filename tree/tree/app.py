from random import random

import toga
from colosseum import CSS


def build(app):
    box = toga.Box(style=CSS(flex=1, padding=0))
    root = {'root': []}
    data_source = toga.DictionaryDataSource(dict({'root': []}))
    # for _ in range(10):
    #     data_source.insert(root, None, 'text {}'.format(_))
    tree = toga.Tree(['Name'], data=data_source, style=CSS(flex=1))

    root_node = data_source.root(0)
    root_node.icon = 'icons/cricket-72.png'



    for _ in reversed(range(100)):
        node = data_source.insert(parent=data_source.root(0), index=0, data=['Job_{}'.format(_)], icon='icons/cricket-72.png')
        if _ % 2 == 0:
            data_source.insert(parent=node, index=0, data='data', icon='icons/cricket-72.png')
        else:
            for _ in range(3):
                node2 = data_source.insert(parent=node, index=0, data='child', icon='icons/cricket-72.png')
                for x in range(3):
                    node3 = data_source.insert(parent=node2, index=0, data='child', icon='icons/cricket-72.png')

    root_node.expanded = True
    box.add(tree)
    # box.add(toga.Button('Button'))
    return box


def main():
    return toga.App('Test Tree', 'org.pybee.tree', startup=build)


if __name__ == '__main__':
    app = main()
    app.main_loop()
