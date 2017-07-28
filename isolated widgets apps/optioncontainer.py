import toga

import time
import toga
from colosseum import CSS

tab_style = CSS(flex=1, padding=20)


def build(app):
    box = toga.Box(children=[toga.Button('My Button')])
    option_container = toga.OptionContainer()
    tab_1_content = toga.Box(children=[toga.Button('Button 1.{}'.format(x)) for x in range(6)], style=tab_style)
    option_container.add('Tab 1', tab_1_content)
    tab_2_content = toga.Box(children=[toga.Button('Button 2.{}'.format(x)) for x in range(6)], style=tab_style)
    option_container.add('Tab 2', tab_2_content)
    tab_3_content = toga.Box(children=[toga.Button('Button 3.{}'.format(x)) for x in range(6)], style=tab_style)
    option_container.add('Tab 3', tab_3_content)
    return option_container


if __name__ == '__main__':
    app = toga.App('Test Slider', 'org.pybee.helloworld', startup=build)
    app.main_loop()
