import toga

import time
import toga
from colosseum import CSS


def build(app):
    box = toga.Box()
    widget = toga.MultilineTextInput(initial='Test Button,\nsuper cool!', style=CSS(flex=1, margin=20))
    box.add(widget)
    return box


if __name__ == '__main__':
    app = toga.App('Test Slider', 'org.pybee.helloworld', startup=build)
    app.main_loop()
