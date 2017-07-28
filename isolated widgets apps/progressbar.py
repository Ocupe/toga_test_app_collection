from random import random

import toga

import time
import toga
from colosseum import CSS




def build(app):
    progressbar = toga.ProgressBar(max=100, value=40, style=CSS(flex=1, margin=20))

    def start_progress(widget):
        progressbar._impl.start()

    def stop_progress(widget):
        progressbar.running = False

    def set_progress(widget):
        progressbar.value = random() * 100

    box = toga.Box()
    box.add(progressbar)
    start_btn = toga.Button('Start', on_press=start_progress)
    stop_btn = toga.Button('Stop', on_press=stop_progress)
    set_btn = toga.Button('Set Random', on_press=set_progress)
    box.add(toga.Box(children=[start_btn, stop_btn, set_btn]))
    return box


if __name__ == '__main__':
    app = toga.App('Test Slider', 'org.pybee.helloworld', startup=build)
    app.main_loop()
