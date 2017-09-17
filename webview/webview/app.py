import toga
from colosseum import CSS


def build(app):
    def on_load(widget):
        print('Finished loading!')
        print(widget.dom)

    def on_key(event, flag):
        print('Key down: ', event, ' Flag: ', flag)

    webview = toga.WebView(on_key_down=on_key, on_webview_load=on_load, style=CSS(flex=1))
    url_input = toga.TextInput(
        initial='https://github.com/',
        style=CSS(flex=1, margin=5)
    )

    def load_page(widget):
        print('loading: ', url_input.value)
        webview.url = url_input.value

    def print_dom(widget):
        print(webview.dom)

    box = toga.Box(
        children=[
            toga.Box(
                children=[
                    url_input,
                    toga.Button('Go', on_press=load_page, style=CSS(width=50)),
                ],
                style=CSS(
                    flex_direction='row',
                    padding_top=25
                )
            ),
            webview,
            toga.Box(
                children=[
                    toga.Button('Print DOM', on_press=print_dom)
                ]
            )
        ],
        style=CSS(
            flex_direction='column'
        )
    )

    webview.url = url_input.value

    # Show the main window
    return box


def main():
    # This needs to return an object that has a main_loop() method.
    return toga.App('Graze', 'org.pybee.graze', startup=build)


if __name__ == '__main__':
    app = main()
    app.main_loop()
