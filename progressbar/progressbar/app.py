from random import random
import toga
from colosseum import CSS


def build(app):
    progressbar = toga.ProgressBar(max=100.3, value=40, style=CSS(flex=1, margin=20))

    def start_progress(widget):
        progressbar._impl.start()

    def stop_progress(widget):
        progressbar.running = False

    def set_progress(widget):
        progressbar.value = random() * 100
        print('Current value: {}'.format(progressbar.value))
        print('Max value: ', progressbar.max)

    box = toga.Box()
    box.add(progressbar)
    start_btn = toga.Button('Start', on_press=start_progress)
    stop_btn = toga.Button('Stop', on_press=stop_progress)
    set_btn = toga.Button('Set Random', on_press=set_progress)
    box.add(toga.Box(children=[start_btn, stop_btn, set_btn]))
    return box


def main():
    return toga.App('Test Slider', 'org.pybee.helloworld', startup=build)


if __name__ == '__main__':
    app = main()
    app.main_loop()
