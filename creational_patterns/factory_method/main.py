from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def render():

    @abstractmethod
    def click():


class HTMLButton(Button):

    def render(self):
        print('Html Render')

    def click(self):
        print('Html click')


class WindowsButton(Button):

    def render(self):
        print('Windows Render')

    def click(self):
        print('Windows click')


class Dialog(ABC):

    def render_window(self):
        button = createButton()
        button.click()
        button.render()

    @abstractmethod
    def create_button():


class HTMLDialog(Dialog):

    def create_button(self):
        return HTMLButton()


class WindowsDialog(Dialog):

    def create_button(self):
        return WindowsButton()


class Client:

    def __init__(self, clietn_type):
        self.dialog = WindowsDialog.create_button() if clietn_type == 'windows' else HTMLDialog.create_button()

    def main(self):
        self.dialog.render()
        self.dialog.click()
