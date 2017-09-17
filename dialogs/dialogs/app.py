""" 'Dialogs Test App'
This little program let's you check whether or not you your dialogs are working the right way.
When pressing a button it should open the corresponding dialog window.
The return value of the dialog is displayed in the label underneath the button that opened it.
"""

import toga
from colosseum import CSS


def build(app):
    # Create labels to display the return values of the dialogs.
    info_label = toga.Label('', style=CSS(margin_bottom=15))
    question_label = toga.Label('', style=CSS(margin_bottom=15))
    confirm_label = toga.Label('', style=CSS(margin_bottom=15))
    error_label = toga.Label('', style=CSS(margin_bottom=15))
    stack_trace_label = toga.Label('', style=CSS(margin_bottom=15))
    save_file_label = toga.Label('', style=CSS(margin_bottom=15))

    # Create callbacks for the buttons to open the dialogs on button press.
    def info(widget):
        return_value = widget.app.main_window.info_dialog('Info', message='This is a info message!')
        print(return_value)
        info_label.text = 'Return Value: {}'.format(return_value)

    def question(widget):
        return_value = widget.app.main_window.question_dialog('Question', message='This is a question message!')
        if return_value:
            print('Question was answered with [YES]')
        else:
            print('Question was answered with [NO]')
        question_label.text = 'Return Value: {}'.format(return_value)

    def confirm(widget):
        return_value = widget.app.main_window.confirm_dialog('Confirm', message='This is a confirm message!')
        if return_value:
            print('Dialog was confirmed. [OK]')
        else:
            print('Dialog was rejected. [CANCEL]')
        confirm_label.text = 'Return Value: {}'.format(return_value)

    def error(widget):
        return_value = widget.app.main_window.error_dialog('Error', message='This is a error message!')
        if return_value is None:
            print('Error dialog was confirmed. [OK]')
        error_label.text = 'Return Value: {}'.format(return_value)

    def stack_trace(widget):
        return_value = widget.app.main_window.stack_trace_dialog('Stack Trace', message='This is a info message!',
                                                                 content='Long Error Messages 0uunyd jöl39u4 lkajf03u2r08 jaoisjf0p3u fp3u90u 09uf\n' * 20)
        stack_trace_label.text = 'Return Value: {}'.format(return_value)

    def save_file(widget):
        path = widget.app.main_window.save_file_dialog('Save File Dialog', suggested_filename='filename',
                                                       file_types=['py'])
        print('Selected Path: {}'.format(path))
        save_file_label.text = 'Return Value: {}'.format(path)

    # Buttons to open the dialogs boxes
    info_btn = toga.Button('Open "Info" Dialog', on_press=info)
    question_btn = toga.Button('Open "Question" Dialog', on_press=question)
    confirm_btn = toga.Button('Open "Confirm" Dialog', on_press=confirm)
    error_btn = toga.Button('Open "Error" Dialog', on_press=error)
    stack_trace_btn = toga.Button('Open "Stack Trace" Dialog', on_press=stack_trace)
    save_file_btn = toga.Button('Open "Save File" Dialog', on_press=save_file)

    # Add buttons and labels to the box and return the box.
    box = toga.Box(style=CSS(padding=30),
                   children=[info_btn, info_label,
                             question_btn, question_label,
                             confirm_btn, confirm_label,
                             error_btn, error_label,
                             stack_trace_btn, stack_trace_label,
                             save_file_btn, save_file_label])
    return box


def main():
    # This needs to return an object that has a main_loop() method.
    return toga.App('Dialogs Test App', 'org.pybee.dialogs', startup=build)

# if __name__ == '__main__':
#     main(
    # ).main_loop()