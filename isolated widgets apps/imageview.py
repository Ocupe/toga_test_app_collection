import time
import toga
from colosseum import CSS


def build(app):
    img_01 = toga.Image(path='icons/brutus-256.png')
    img_02 = toga.Image(path='https://dict.leo.org/img/leo/160x60/schriftzug-222990a1.png')

    image_view_01 = toga.ImageView(image=img_01)
    image_view_02 = toga.ImageView(image=img_02)
    box = toga.Box(style=CSS(flex=1))
    box.add(image_view_01)
    return box
    return image_view_02

if __name__ == '__main__':
    app = toga.App('Test Table', 'org.pybee.helloworld', startup=build)
    app.main_loop()
