import time
import toga
from colosseum import CSS


def build(app):
    text_input_1 = toga.MultilineTextInput(initial='Test Button,\nsuper cool!', style=CSS(flex=1, margin=20))
    text_input_2 = toga.MultilineTextInput(placeholder='This is a placeholder', style=CSS(flex=1, margin=20))
    text_input_3 = toga.MultilineTextInput(initial='Read Only', readonly=True, style=CSS(flex=1, margin=20))

    def callback(widget):
        text_input_1.value = 'New Text: {}'.format(time.time())

    def callback_clear(widget):
        text_input_1.clear()

    btn_1 = toga.Button('Set Text', on_press=callback)
    btn_2 = toga.Button('Clear Text', on_press=callback_clear)

    box = toga.Box(children=[text_input_1, btn_1, btn_2, text_input_2, text_input_3],
                   style=CSS(padding=20))
    return box


def main():
    # This needs to return an object that has a main_loop() method.
    return toga.App('Test MultilineTextInput', 'org.pybee.helloworld', startup=build)


if __name__ == '__main__':
    app = main()
    app.main_loop()
