import toga
from colosseum import CSS


def build(app):
    password_input = toga.PasswordInput()
    def callback(widget):
        print(password_input.value)
        password_input.clear()
    btn = toga.Button('Print Password & Clear', on_press=callback)
    return toga.Box(style=CSS(flex=1, padding=20), children=[password_input, btn])


def main():
    return toga.App('Test Table', 'org.pybee.helloworld', startup=build)

if __name__ == '__main__':
    app = main()
    app.main_loop()
