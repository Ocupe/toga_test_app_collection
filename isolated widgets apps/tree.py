import time
import toga
from colosseum import CSS


def build(app):
    tree = toga.Tree(headings=['First Heading', 'Second Heading'])
    tree._impl.insert(None, 10, 'first', 'second')
    return tree

if __name__ == '__main__':
    app = toga.App('Test Table', 'org.pybee.helloworld', startup=build)
    app.main_loop()
