from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.pickers import MDDatePicker
from kivy.uix.screenmanager import FadeTransition
import yaml

Window.size = 400, 700


class MyRoot(MDScreenManager):

    def return_settings_data(self, value):
        with open('settings.yaml', 'r') as s_d:
            data = yaml.safe_load(s_d)
        return data[value]

    def set_settings_data(self, value):
        with open('settings.yaml', 'w') as s_d:
            yaml.dump(value, s_d)

    def cmc(self):
        pass

class MyApp(MDApp, MyRoot):
    def build(self):
        self.title = 'myapp'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return MyRoot()


if __name__ == "__main__":
    MyApp().run()
