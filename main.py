from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.pickers import MDDatePicker
from kivy.uix.screenmanager import FadeTransition
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
import json

Window.size = 400, 700

with open('settings.json', 'r') as s_d:
    data = json.load(s_d)


class MyRoot(MDScreenManager):

    def return_settings_data(self, value):
        return data[value]

    def set_settings_data(self, key, value):
        data[key] = value

    def add_tracking_element(self):
        self.ids.mybox.add_widget(MDTextField(hint_text='What will tracking?'))

    def tye(self, value):
        for i in value:
            print(i.text)

class MyApp(MDApp, MyRoot):
    def build(self):
        self.title = 'myapp'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return MyRoot()

    def on_start(self):
        pass

    def on_stop(self):
        with open('settings.json', 'w') as f:
            json.dump(data, f)


if __name__ == "__main__":
    MyApp().run()
