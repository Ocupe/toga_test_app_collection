import toga

import time
import toga
from colosseum import CSS

tab_style = CSS(flex=1, padding=20)


def build(app):
    font = toga.Font('Helvetica', 40)
    return toga.Box(children=[toga.Button('Button')])


def main():
    return toga.App('Test Font', 'org.pybee.font', startup=build)


if __name__ == '__main__':
    app = main()
    app.main_loop()
