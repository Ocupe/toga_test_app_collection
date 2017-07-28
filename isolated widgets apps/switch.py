import time
import toga
from colosseum import CSS


def build(app):
    def callback(widget):
        label.text = 'Switch State: {}'.format(widget.is_on)

    def btn_callback(widget):
        switch.label = str('Update Label: {}'.format(time.strftime('%H:%M:%S')))
        switch.is_on = True if switch.is_on is False else False
        label.text = 'Switch State: {}'.format(switch.is_on)

    def enable_callback(widget):
        switch.enabled = True if switch.enabled is False else False

    switch = toga.Switch('My Switch', on_toggle=callback)
    button = toga.Button('Check/Uncheck Switch', on_press=btn_callback, style=CSS(width=200))
    enable_btn = toga.Button('Enable/Disable Switch', on_press=enable_callback, style=CSS(width=200))
    label = toga.Label('Switch State: {}'.format(switch.is_on))

    style = CSS(flex=1, padding=10, margin_top=50)
    box = toga.Box(style=style)
    box.add(switch)
    box.add(button)
    box.add(enable_btn)
    box.add(label)
    return box


if __name__ == '__main__':
    app = toga.App('Test Switch', 'org.pybee.helloworld', startup=build)
    app.main_loop()
