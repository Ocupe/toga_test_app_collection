import toga

import time
import toga
from colosseum import CSS

tab_style = CSS(flex=1, padding=20)


def build(app):
    font = toga.Font('Helvetica', 20)
    return toga.Box(children=[toga.Button('Button')])


if __name__ == '__main__':
    app = toga.App('Test Slider', 'org.pybee.helloworld', startup=build)
    app.main_loop()
