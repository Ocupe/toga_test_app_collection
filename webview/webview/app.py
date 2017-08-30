import toga
from colosseum import CSS


class Graze(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(self.name)
        self.main_window.app = self

        self.webview = toga.WebView(style=CSS(flex=1))
        self.url_input = toga.TextInput(
            initial='https://github.com/',
            style=CSS(flex=1, margin=5)
        )

        box = toga.Box(
            children=[
                toga.Box(
                    children=[
                        self.url_input,
                        toga.Button('Go', on_press=self.load_page, style=CSS(width=50)),
                    ],
                    style=CSS(
                        flex_direction='row'
                    )
                ),
                self.webview,
            ],
            style=CSS(
                flex_direction='column'
            )
        )

        self.main_window.content = box
        self.webview.url = self.url_input.value

        # Show the main window
        self.main_window.show()

    def load_page(self, widget):
        print('loading: ', self.url_input.value)
        self.webview.url = self.url_input.value


def main():
    # This needs to return an object that has a main_loop() method.
    return Graze('Graze', 'org.pybee.graze')


if __name__ == '__main__':
    app = main()
    app.main_loop()
